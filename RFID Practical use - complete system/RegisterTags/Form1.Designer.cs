namespace ReaderApp
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            txtTagId = new TextBox();
            btnRed = new Button();
            groupBox1 = new GroupBox();
            txtColor = new TextBox();
            btnWhite = new Button();
            btnYellow = new Button();
            btnBlack = new Button();
            btnBlue = new Button();
            btnGreen = new Button();
            label1 = new Label();
            txtTagName = new TextBox();
            label2 = new Label();
            btnRegister = new Button();
            dgvView = new DataGridView();
            cboTags = new ComboBox();
            btnDeleteTag = new Button();
            groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)dgvView).BeginInit();
            SuspendLayout();
            // 
            // txtTagId
            // 
            txtTagId.Location = new Point(43, 54);
            txtTagId.Name = "txtTagId";
            txtTagId.Size = new Size(256, 23);
            txtTagId.TabIndex = 0;
            txtTagId.KeyDown += txtTagId_KeyDown;
            txtTagId.KeyPress += txtTagId_KeyPress;
            // 
            // btnRed
            // 
            btnRed.BackColor = Color.Red;
            btnRed.Location = new Point(6, 22);
            btnRed.Name = "btnRed";
            btnRed.Size = new Size(75, 23);
            btnRed.TabIndex = 1;
            btnRed.Text = "Rød";
            btnRed.UseVisualStyleBackColor = false;
            btnRed.Click += btnRed_Click;
            // 
            // groupBox1
            // 
            groupBox1.Controls.Add(txtColor);
            groupBox1.Controls.Add(btnWhite);
            groupBox1.Controls.Add(btnYellow);
            groupBox1.Controls.Add(btnBlack);
            groupBox1.Controls.Add(btnBlue);
            groupBox1.Controls.Add(btnGreen);
            groupBox1.Controls.Add(btnRed);
            groupBox1.Location = new Point(43, 83);
            groupBox1.Name = "groupBox1";
            groupBox1.Size = new Size(256, 116);
            groupBox1.TabIndex = 2;
            groupBox1.TabStop = false;
            groupBox1.Text = "Farge";
            // 
            // txtColor
            // 
            txtColor.Location = new Point(75, 80);
            txtColor.Name = "txtColor";
            txtColor.ReadOnly = true;
            txtColor.Size = new Size(100, 23);
            txtColor.TabIndex = 7;
            // 
            // btnWhite
            // 
            btnWhite.BackColor = Color.White;
            btnWhite.Location = new Point(168, 51);
            btnWhite.Name = "btnWhite";
            btnWhite.Size = new Size(75, 23);
            btnWhite.TabIndex = 6;
            btnWhite.Text = "Hvit";
            btnWhite.UseVisualStyleBackColor = false;
            btnWhite.Click += btnWhite_Click;
            // 
            // btnYellow
            // 
            btnYellow.BackColor = Color.Yellow;
            btnYellow.Location = new Point(168, 22);
            btnYellow.Name = "btnYellow";
            btnYellow.Size = new Size(75, 23);
            btnYellow.TabIndex = 5;
            btnYellow.Text = "Gul";
            btnYellow.UseVisualStyleBackColor = false;
            btnYellow.Click += btnYellow_Click;
            // 
            // btnBlack
            // 
            btnBlack.BackColor = Color.Black;
            btnBlack.ForeColor = Color.White;
            btnBlack.Location = new Point(87, 51);
            btnBlack.Name = "btnBlack";
            btnBlack.Size = new Size(75, 23);
            btnBlack.TabIndex = 4;
            btnBlack.Text = "Svart";
            btnBlack.UseVisualStyleBackColor = false;
            btnBlack.Click += btnBlack_Click;
            // 
            // btnBlue
            // 
            btnBlue.BackColor = Color.Blue;
            btnBlue.ForeColor = Color.White;
            btnBlue.Location = new Point(87, 22);
            btnBlue.Name = "btnBlue";
            btnBlue.Size = new Size(75, 23);
            btnBlue.TabIndex = 3;
            btnBlue.Text = "Blå";
            btnBlue.UseVisualStyleBackColor = false;
            btnBlue.Click += btnBlue_Click;
            // 
            // btnGreen
            // 
            btnGreen.BackColor = Color.Green;
            btnGreen.Location = new Point(6, 51);
            btnGreen.Name = "btnGreen";
            btnGreen.Size = new Size(75, 23);
            btnGreen.TabIndex = 2;
            btnGreen.Text = "Grønn";
            btnGreen.UseVisualStyleBackColor = false;
            btnGreen.Click += btnGreen_Click;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(43, 36);
            label1.Name = "label1";
            label1.Size = new Size(62, 15);
            label1.TabIndex = 3;
            label1.Text = "RFID TagId";
            // 
            // txtTagName
            // 
            txtTagName.Enabled = false;
            txtTagName.Location = new Point(111, 205);
            txtTagName.Name = "txtTagName";
            txtTagName.Size = new Size(188, 23);
            txtTagName.TabIndex = 4;
            txtTagName.KeyDown += txtTagName_KeyDown;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(43, 208);
            label2.Name = "label2";
            label2.Size = new Size(62, 15);
            label2.TabIndex = 5;
            label2.Text = "Tag Navn :";
            // 
            // btnRegister
            // 
            btnRegister.Enabled = false;
            btnRegister.Location = new Point(111, 260);
            btnRegister.Name = "btnRegister";
            btnRegister.Size = new Size(122, 42);
            btnRegister.TabIndex = 6;
            btnRegister.Text = "Registrer RFID Tag";
            btnRegister.UseVisualStyleBackColor = true;
            btnRegister.Click += btnRegister_Click;
            // 
            // dgvView
            // 
            dgvView.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dgvView.Location = new Point(339, 36);
            dgvView.Name = "dgvView";
            dgvView.RowTemplate.Height = 25;
            dgvView.Size = new Size(321, 252);
            dgvView.TabIndex = 7;
            // 
            // cboTags
            // 
            cboTags.DropDownStyle = ComboBoxStyle.DropDownList;
            cboTags.FormattingEnabled = true;
            cboTags.Location = new Point(339, 294);
            cboTags.Name = "cboTags";
            cboTags.Size = new Size(240, 23);
            cboTags.TabIndex = 8;
            // 
            // btnDeleteTag
            // 
            btnDeleteTag.Location = new Point(585, 293);
            btnDeleteTag.Name = "btnDeleteTag";
            btnDeleteTag.Size = new Size(75, 23);
            btnDeleteTag.TabIndex = 9;
            btnDeleteTag.Text = "Slett Tag";
            btnDeleteTag.UseVisualStyleBackColor = true;
            btnDeleteTag.Click += btnDeleteTag_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(703, 375);
            Controls.Add(btnDeleteTag);
            Controls.Add(cboTags);
            Controls.Add(dgvView);
            Controls.Add(btnRegister);
            Controls.Add(label2);
            Controls.Add(txtTagName);
            Controls.Add(label1);
            Controls.Add(groupBox1);
            Controls.Add(txtTagId);
            Name = "Form1";
            Text = "Tag Register";
            groupBox1.ResumeLayout(false);
            groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)dgvView).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private TextBox txtTagId;
        private Button btnRed;
        private GroupBox groupBox1;
        private Button btnWhite;
        private Button btnYellow;
        private Button btnBlack;
        private Button btnBlue;
        private Button btnGreen;
        private TextBox txtColor;
        private Label label1;
        private TextBox txtTagName;
        private Label label2;
        private Button btnRegister;
        private DataGridView dgvView;
        private ComboBox cboTags;
        private Button btnDeleteTag;
    }
}