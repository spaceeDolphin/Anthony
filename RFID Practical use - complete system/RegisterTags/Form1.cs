using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Linq;

namespace ReaderApp
{
    public partial class Form1 : Form
    {
        string databaseConfig = ConfigurationManager.ConnectionStrings["BikeShare"].ConnectionString;

        //For å hente alle tags i TAG entiteten
        string availableTags = @"SELECT TagId FROM TAG;";
        public Form1()
        {
            InitializeComponent();
            Reset();
            ShowAllTags();
            UpdateComboBoxes();
        }

        void ViewDataGridView(string sqlQuery)
        {
            SqlConnection connDatabase = new SqlConnection(databaseConfig);
            SqlDataAdapter sda;
            DataTable dataTable;
            dgvView.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.AllCells;
            try
            {
                connDatabase.Open();
                sda = new SqlDataAdapter(sqlQuery, connDatabase);
                dataTable = new DataTable();
                sda.Fill(dataTable);
                dgvView.DataSource = dataTable;
                connDatabase.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
                throw;
            }
        }

        //Vise alle tags i TAG entiteten
        void ShowAllTags()
        {
            string sqlQuery = @"SELECT * FROM ViewRegisteredTags";
            ViewDataGridView(sqlQuery);
        }

        void Reset()
        {
            txtTagId.Clear();
            txtTagId.Enabled = true;
            txtColor.Text = "white";
            txtTagName.Clear();
            btnRegister.Enabled = false;
        }

        void FillComboBox(ComboBox cboBox, string sqlQuery)
        {
            //Henter ut alle verdier i en kollonne og setter inn i en Combo Box
            try
            {
                SqlConnection connDatabase = new SqlConnection(databaseConfig);
                SqlCommand sql = new SqlCommand(sqlQuery, connDatabase);
                connDatabase.Open();
                SqlDataReader dr = sql.ExecuteReader();
                string? retrievedTableValue;
                cboBox.Items.Clear();
                while (dr.Read() == true)
                {
                    retrievedTableValue = dr[0].ToString();
                    cboBox.Items.Add(retrievedTableValue);
                }
                connDatabase.Close();
                cboBox.SelectedIndex = 0;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
        //Plassere alle tags i combobox, slik at man kan velge og slette en eksisterende tag
        void UpdateComboBoxes()
        {
            FillComboBox(cboTags, availableTags);
        }

        private void btnRed_Click(object sender, EventArgs e)
        {
            txtColor.Text = "red";
        }

        private void btnBlue_Click(object sender, EventArgs e)
        {
            txtColor.Text = "blue";
        }

        private void btnYellow_Click(object sender, EventArgs e)
        {
            txtColor.Text = "yellow";
        }

        private void btnGreen_Click(object sender, EventArgs e)
        {
            txtColor.Text = "green";
        }

        private void btnBlack_Click(object sender, EventArgs e)
        {
            txtColor.Text = "black";
        }

        private void btnWhite_Click(object sender, EventArgs e)
        {
            txtColor.Text = "white";
        }

        //Registrere tag, bruker klasse Tag
        private void btnRegister_Click(object sender, EventArgs e)
        {
            string tagId = txtTagId.Text;
            string tagColor = txtColor.Text;
            string tagText = txtTagName.Text;
            if (cboTags.FindString(tagId) == -1)
            {
                Tag tag = new Tag(tagId, tagColor, tagText);
                tag.RegisterTag(databaseConfig);
            }
            else
            {
                MessageBox.Show("Denne tag-en er allerede registrert");
            }

            Reset();
            ShowAllTags();
            UpdateComboBoxes();
        }

        private void txtTagId_KeyPress(object sender, KeyPressEventArgs e)
        {
        }

        private void txtTagId_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                string tagId = txtTagId.Text;
                if (tagId != "")
                {
                    txtTagId.Enabled = false;
                    txtTagName.Enabled = true;
                }
                else
                {
                    MessageBox.Show("Feilmelding: Tomt felt. Registrer TagId");
                }
            }
        }

        private void txtTagName_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                string tagName = txtTagName.Text;
                if (tagName != "")
                {
                    txtTagName.Enabled = false;
                    btnRegister.Enabled = true;
                }
                else
                {
                    MessageBox.Show("Feilmelding: Tomt felt. Registrer Tag Navn");
                }
            }
        }

        //Slette tag, bruker klasse Tag
        private void btnDeleteTag_Click(object sender, EventArgs e)
        {
            string tagId = cboTags.Text;
            Tag tag = new Tag(tagId);
            tag.DeleteTag(databaseConfig);
            ShowAllTags();
            UpdateComboBoxes();
        }
    }
}