using BikeShareWeb.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore.Metadata.Internal;
using Newtonsoft.Json.Linq;
using System.Data.SqlClient;

namespace BikeShareWeb.Views.Home
{
    public class StatisticsModel : PageModel
    {
        public List<BikeUnlock> bikeUnlocks = new List<BikeUnlock>();
        public void OnGet()
        {


            try
            {
                String databaseConfig = "Data Source=localhost\\sqlexpress;Initial Catalog=BikeShareDatabase;Integrated Security=True";
                String sqlQuery = "Exec GetBikeUnlocks @tagId = E2B0E91B;";
                using (SqlConnection conn = new SqlConnection(databaseConfig))
                {
                    conn.Open();
                    using (SqlCommand command = new SqlCommand(sqlQuery, conn))
                    {
                        using (SqlDataReader reader = command.ExecuteReader())
                        {
                            while (reader.Read())
                            {
                                BikeUnlock bikeUnlock = new BikeUnlock();
                                bikeUnlock.unlockTime = reader.GetDateTime(0).ToString();
                                bikeUnlock.stationName = reader.GetString(1);
                                bikeUnlock.bikeName = reader.GetString(2);
                                bikeUnlocks.Add(bikeUnlock);
                            }
                        }
                    }
                    conn.Close();

                }
            }
            catch (Exception ex) { }
        }
    }
}
