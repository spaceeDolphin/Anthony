using Microsoft.IdentityModel.Protocols;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Linq;

namespace BikeOS
{
    public class BikeToggle:Bike,ILockable
    {
        private string databaseConfig = ConfigurationManager.ConnectionStrings["BikeShare"].ConnectionString;
        private string? getStatus;
        public int StationId { get; set; }
        public int BikeId { get; set; }
        public string TagId { get; set; }
        public BikeToggle(string tagId, int bikeId, int stationId) : base(id:bikeId)
        {
            TagId = tagId;
            BikeId = bikeId;
            StationId = stationId;
        }

        //Følgende bruker stored procedures i BikeShareDatabase
        public void RegisterLock()
        {
            string newStatus = "Locked";
            try
            {
                SqlConnection connDatabase = new SqlConnection(databaseConfig);
                SqlCommand sql = new SqlCommand("InsertLock", connDatabase);
                sql.CommandType = CommandType.StoredProcedure;
                connDatabase.Open();
                sql.Parameters.Add(new SqlParameter("@stationId", StationId));
                sql.Parameters.Add(new SqlParameter("@tagId", TagId));
                sql.Parameters.Add(new SqlParameter("@bikeId", BikeId));
                sql.ExecuteNonQuery();

                sql = new SqlCommand("UpdateLock", connDatabase);
                sql.CommandType = CommandType.StoredProcedure;
                sql.Parameters.Add(new SqlParameter("@bikeId", BikeId));
                sql.Parameters.Add(new SqlParameter("@lockStatus", newStatus));
                sql.ExecuteNonQuery();
                connDatabase.Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                throw;
            }
        }

        public void RegisterUnlock()
        {
            string newStatus = "Unlocked";
            try
            {
                SqlConnection connDatabase = new SqlConnection(databaseConfig);
                SqlCommand sql = new SqlCommand("InsertUnlock", connDatabase);
                sql.CommandType = CommandType.StoredProcedure;
                connDatabase.Open();
                sql.Parameters.Add(new SqlParameter("@stationId", StationId));
                sql.Parameters.Add(new SqlParameter("@tagId", TagId));
                sql.Parameters.Add(new SqlParameter("@bikeId", BikeId));
                sql.ExecuteNonQuery();

                sql = new SqlCommand("UpdateLock", connDatabase);
                sql.CommandType = CommandType.StoredProcedure;
                sql.Parameters.Add(new SqlParameter("@bikeId", BikeId));
                sql.Parameters.Add(new SqlParameter("@lockStatus", newStatus));
                sql.ExecuteNonQuery();
                connDatabase.Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                throw;
            }
        }

        public string GetBikeStatus()
        {
            string status = "";
            getStatus = @$"SELECT LockStatus FROM BIKE WHERE BikeId = {BikeId};";
            try
            {
                SqlConnection connDatabase = new SqlConnection(databaseConfig);
                SqlCommand sql = new SqlCommand(getStatus, connDatabase);
                connDatabase.Open();
                SqlDataReader dr = sql.ExecuteReader();
                string? retrievedTableValue;
                while (dr.Read() == true)
                {
                    retrievedTableValue = dr[0].ToString();
                    status = retrievedTableValue;
                }
                connDatabase.Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            return status;
        }
    }
}
