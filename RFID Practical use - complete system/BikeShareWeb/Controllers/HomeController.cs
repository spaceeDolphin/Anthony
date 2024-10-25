using BikeShareWeb.Areas.Identity.Data;
using BikeShareWeb.Models;
using BikeShareWeb.Views.Home;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore.Metadata.Internal;
using Newtonsoft.Json.Linq;
using System.Diagnostics;

namespace BikeShareWeb.Controllers
{
    [Authorize]
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        private readonly UserManager<ApplicationUser> _userManager;

        public HomeController(ILogger<HomeController> logger, UserManager<ApplicationUser> userManager)
        {
            _logger = logger;
            this._userManager = userManager;
        }

        public IActionResult Index()
        {

            #region BikeData
            Bike bike1 = new Bike(1);
            ViewData["Bike1Name"] = bike1.BikeName;
            ViewData["Bike1Status"] = bike1.BikeStatus;
            ViewData["Bike1Position"] = bike1.BikePosition;
            ViewData["Bike1Use"] = bike1.BikeUse;
            Bike bike2 = new Bike(2);
            ViewData["Bike2Name"] = bike2.BikeName;
            ViewData["Bike2Status"] = bike2.BikeStatus;
            ViewData["Bike2Position"] = bike2.BikePosition;
            ViewData["Bike2Use"] = bike2.BikeUse;
            Bike bike3 = new Bike(3);
            ViewData["Bike3Name"] = bike3.BikeName;
            ViewData["Bike3Status"] = bike3.BikeStatus;
            ViewData["Bike3Position"] = bike3.BikePosition;
            ViewData["Bike3Use"] = bike3.BikeUse;
            Bike bike4 = new Bike(4);
            ViewData["Bike4Name"] = bike4.BikeName;
            ViewData["Bike4Status"] = bike4.BikeStatus;
            ViewData["Bike4Position"] = bike4.BikePosition;
            ViewData["Bike4Use"] = bike4.BikeUse;
            Bike bike5 = new Bike(5);
            ViewData["Bike5Name"] = bike5.BikeName;
            ViewData["Bike5Status"] = bike5.BikeStatus;
            ViewData["Bike5Position"] = bike5.BikePosition;
            ViewData["Bike5Use"] = bike5.BikeUse;
            Bike bike6 = new Bike(6);
            ViewData["Bike6Name"] = bike6.BikeName;
            ViewData["Bike6Status"] = bike6.BikeStatus;
            ViewData["Bike6Position"] = bike6.BikePosition;
            ViewData["Bike6Use"] = bike6.BikeUse;
            Bike bike7 = new Bike(7);
            ViewData["Bike7Name"] = bike7.BikeName;
            ViewData["Bike7Status"] = bike7.BikeStatus;
            ViewData["Bike7Position"] = bike7.BikePosition;
            ViewData["Bike7Use"] = bike7.BikeUse;
            Bike bike8 = new Bike(8);
            ViewData["Bike8Name"] = bike8.BikeName;
            ViewData["Bike8Status"] = bike8.BikeStatus;
            ViewData["Bike8Position"] = bike8.BikePosition;
            ViewData["Bike8Use"] = bike8.BikeUse;
            Bike bike9 = new Bike(9);
            ViewData["Bike9Name"] = bike9.BikeName;
            ViewData["Bike9Status"] = bike9.BikeStatus;
            ViewData["Bike9Position"] = bike9.BikePosition;
            ViewData["Bike9Use"] = bike9.BikeUse;
            #endregion
            return View();
        }

        public IActionResult Privacy()
        {
            return View();
        }

        public IActionResult Map()
        {
            return View();
        }

        public IActionResult Statistics()
        {
            string? userId;
            userId = _userManager.GetUserId(this.User).ToString();
            TagUser tagUser = new TagUser(userId);
            ViewData["myKey"] = tagUser.UserKey;
            //ViewData["myKey"] = "142E37CF";
            return View();
        }

        public IActionResult Connect()
        {
            ViewData["UserID"] = _userManager.GetUserId(this.User);
            return View();
        }

        [HttpPost]
        public IActionResult Connect(UserTag userTag)
        {
            string? userId;
            string commandResult;
            userId = _userManager.GetUserId(this.User).ToString();
            userTag.UserId = userId;
            ViewData["UserID"] = userId;
            string userKey = userTag.UserKey;
            commandResult = userTag.InsertUserTag();
            ViewData["CommandResult"] = commandResult;
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}