using Microsoft.EntityFrameworkCore.Metadata.Internal;
using Newtonsoft.Json.Linq;
using System.Data.SqlClient;

namespace BikeShareWeb.Models
{
    public class UserTag
    {
        private String databaseConfig;
        public string UserKey { get; set; }
        public string UserId { get; set; }
        public string InsertUserTag()
        {
            string commandResult = "RFID key " + UserKey + " registered to user";
            try
            {
                databaseConfig = "Data Source=localhost\\sqlexpress;Initial Catalog=BikeShareDatabase;Integrated Security=True";
                using (SqlConnection conn = new SqlConnection(databaseConfig))
                {
                    conn.Open();
                    using (SqlCommand command = new SqlCommand("InsertUserTag", conn))
                    {
                        command.CommandType = System.Data.CommandType.StoredProcedure;
                        command.Parameters.Add(new SqlParameter("@userId", UserId));
                        command.Parameters.Add(new SqlParameter("@userKey", UserKey));
                        command.ExecuteNonQuery();
                    }
                    conn.Close();

                }
            }
            catch (Exception ex) 
            {
                commandResult = ex.Message;
            }
            return commandResult;
        }
    }
}
