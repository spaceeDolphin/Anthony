using System.Configuration;
using System.Data;
using System.Data.SqlClient;

namespace BikeShareWeb.Models
{
    public class Bike
    {
        private String databaseConfig;
        public string BikeName { get; set; }
        public string BikeStatus { get; set; }
        public string BikePosition { get; set; }
        public string BikeUse { get; set; }
        public int BikeId { get; set; }
        public Bike(int bikeId)
        {
            BikeId = bikeId;
            try
            {
                databaseConfig = "Data Source=localhost\\sqlexpress;Initial Catalog=BikeShareDatabase;Integrated Security=True";
            }
            catch (Exception ex) { }

            GetBikeValues(out string bikeName, out string bikeStatus, out string bikePosition, out string bikeUse);
            BikeName = bikeName;
            BikeStatus = bikeStatus;
            BikePosition = bikePosition;
            BikeUse = bikeUse;
        }
        public Bike()
        {
            BikeName = "Bike";
            BikeStatus = "N/A";
            BikePosition = "N/A";
            BikeUse = "N/A";
            BikeId = 0;
        }
        public void GetBikeValues(out string bikeName, out string bikeStatus, out string bikePosition, out string bikeUse)
        {
            string bikeStatusTime;
            string bikeNameSqlQuery = $"SELECT BikeName FROM BIKE WHERE BikeId = {BikeId}";
            String bikeStatusSqlQuery = $"SELECT LockStatus FROM BIKE WHERE BikeId = {BikeId}";
            String bikePositionSqlQuery = @$"SELECT TOP 1 StationName 
                FROM BIKE_LOCK AS BL, BIKE_STATION AS BS
                WHERE BS.StationId = BL.StationId
                AND BikeId = {BikeId}
                ORDER BY LockTime DESC;";
            String bikeStatusTimeSqlQuery = @$"SELECT TOP 1 LockTime
                FROM BIKE_LOCK
                WHERE BikeId = {BikeId}
                ORDER BY LockTime DESC;";

            bikeName = GetBikeValue(bikeNameSqlQuery);
            bikeStatus = GetBikeValue(bikeStatusSqlQuery);
            bikePosition = GetBikeValue(bikePositionSqlQuery);
            bikeStatusTime = GetBikeValue(bikeStatusTimeSqlQuery);
            bikeUse = bikeStatusTime;
        }

        public string GetBikeValue(String sqlQuery)
        {
            string value = "not found";
            try
            {
                using (SqlConnection conn = new SqlConnection(databaseConfig))
                {
                    conn.Open();
                    using (SqlCommand command = new SqlCommand(sqlQuery, conn))
                    {
                        using (SqlDataReader reader = command.ExecuteReader())
                        {
                            while(reader.Read())
                            {
                                value = reader[0].ToString();
                            }
                        }
                    }
                    conn.Close();

                }
            }
            catch (Exception ex) { }
            if (value == null) { value = "not found"; }
            return value;
        }

        //public string GetBikeValue(string sqlQuery)
        //{
        //    string value = "";
        //    try
        //    {
        //        SqlConnection connDatabase = new SqlConnection(databaseConfig);
        //        SqlCommand sql = new SqlCommand(sqlQuery, connDatabase);
        //        connDatabase.Open();
        //        SqlDataReader dr = sql.ExecuteReader();
        //        string? retrievedTableValue;
        //        while (dr.Read() == true)
        //        {
        //            retrievedTableValue = dr[0].ToString();
        //            value = retrievedTableValue;
        //        }
        //        connDatabase.Close();
        //    }
        //    catch (Exception ex)
        //    {
        //    }
        //    if (value == null) { value = "n/a"; }
        //    return value;
        //}
    }
}
