using Microsoft.EntityFrameworkCore.Metadata.Internal;
using System.Data.SqlClient;

namespace BikeShareWeb.Models
{
    public class TagUser
    {
        public string UserId { get; set; }
        public string UserKey { get; set; }
        public TagUser(string userId)
        {
            UserId = userId;
            GetKey();
        }
        public void GetKey()
        {
            UserKey = "not found";
            String databaseConfig = "Data Source=localhost\\sqlexpress;Initial Catalog=BikeShareDatabase;Integrated Security=True";
            String sqlQuery = $"SELECT UserKey FROM USER_TAG WHERE UserId LIKE '{UserId}';";
            List<BikeUnlock> bikeUnlocks = new List<BikeUnlock>();
            try
            {
                string retrievedValue;
                using (SqlConnection conn = new SqlConnection(databaseConfig))
                {
                    conn.Open();
                    using (SqlCommand command = new SqlCommand(sqlQuery, conn))
                    {
                        using (SqlDataReader reader = command.ExecuteReader())
                        {
                            while (reader.Read())
                            {
                                retrievedValue = reader.GetString(0);
                                UserKey = retrievedValue;
                            }
                        }
                    }
                    conn.Close();

                }
            }
            catch (Exception ex) {  }
        }
    }
}
