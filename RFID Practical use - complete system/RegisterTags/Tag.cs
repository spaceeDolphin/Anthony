using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Linq;

namespace ReaderApp
{
    public class Tag
    {
        public string TagId { get; set; }
        public string TagColor { get; set; }
        public string TagText { get; set; }

        public Tag(string tagId, string tagColor, string tagText)
        {
            TagId = tagId;
            TagColor = tagColor;
            TagText = tagText;
        }

        public Tag(string tagId)
        {
            TagId = tagId;
            TagColor = "white";
            TagText = "tag";
        }

        //Følgende bruker stored procedures i BikeShareDatabase
        public void RegisterTag(string databaseConfig)
        {
            try
            {
                SqlConnection connDatabase = new SqlConnection(databaseConfig);
                SqlCommand sql = new SqlCommand("InsertTag", connDatabase);
                sql.CommandType = CommandType.StoredProcedure;
                connDatabase.Open();
                sql.Parameters.Add(new SqlParameter("@tagId", TagId));
                sql.Parameters.Add(new SqlParameter("@tagColor", TagColor));
                sql.Parameters.Add(new SqlParameter("@tagText", TagText));
                sql.ExecuteNonQuery();
                connDatabase.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
                throw;
            }
        }
        public void DeleteTag(string databaseConfig)
        {
            try
            {
                SqlConnection connDatabase = new SqlConnection(databaseConfig);
                SqlCommand sql = new SqlCommand("DeleteTag", connDatabase);
                sql.CommandType = CommandType.StoredProcedure;
                connDatabase.Open();
                sql.Parameters.Add(new SqlParameter("@tagId", TagId));
                sql.ExecuteNonQuery();
                connDatabase.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
                throw;
            }
        }
    }
}
