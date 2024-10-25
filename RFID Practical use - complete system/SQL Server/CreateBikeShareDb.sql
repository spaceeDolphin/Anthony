CREATE DATABASE [BikeShareDatabase]
GO
USE [BikeShareDatabase]
GO
/****** Object:  Table [dbo].[AspNetUsers]    Script Date: 01/11/2023 21:15:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[AspNetUsers](
	[Id] [nvarchar](450) NOT NULL,
	[FirstName] [nvarchar](100) NOT NULL,
	[LastName] [nvarchar](100) NOT NULL,
	[UserName] [nvarchar](256) NULL,
	[NormalizedUserName] [nvarchar](256) NULL,
	[Email] [nvarchar](256) NULL,
	[NormalizedEmail] [nvarchar](256) NULL,
	[EmailConfirmed] [bit] NOT NULL,
	[PasswordHash] [nvarchar](max) NULL,
	[SecurityStamp] [nvarchar](max) NULL,
	[ConcurrencyStamp] [nvarchar](max) NULL,
	[PhoneNumber] [nvarchar](max) NULL,
	[PhoneNumberConfirmed] [bit] NOT NULL,
	[TwoFactorEnabled] [bit] NOT NULL,
	[LockoutEnd] [datetimeoffset](7) NULL,
	[LockoutEnabled] [bit] NOT NULL,
	[AccessFailedCount] [int] NOT NULL,
 CONSTRAINT [PK_AspNetUsers] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TAG]    Script Date: 01/11/2023 21:15:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TAG](
	[TagId] [varchar](30) NOT NULL,
	[TagColor] [varchar](30) NULL,
	[TagText] [varchar](30) NULL,
 CONSTRAINT [XPKTAG] PRIMARY KEY CLUSTERED 
(
	[TagId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[USER_TAG]    Script Date: 01/11/2023 21:15:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[USER_TAG](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[UserId] [nvarchar](450) NULL,
	[UserKey] [varchar](30) NULL,
PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[ViewRegisteredTags]    Script Date: 01/11/2023 21:15:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[ViewRegisteredTags] AS
SELECT TagId AS [RFID], TagColor AS Farge, TagText AS [Type], Email AS Bruker
FROM USER_TAG AS UT 
RIGHT JOIN TAG
ON TAG.TagId = UT.UserKey
LEFT JOIN AspNetUsers AS U
ON U.Id = UT.UserId
GO
/****** Object:  Table [dbo].[__EFMigrationsHistory]    Script Date: 01/11/2023 21:15:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[__EFMigrationsHistory](
	[MigrationId] [nvarchar](150) NOT NULL,
	[ProductVersion] [nvarchar](32) NOT NULL,
 CONSTRAINT [PK___EFMigrationsHistory] PRIMARY KEY CLUSTERED 
(
	[MigrationId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[AspNetRoleClaims]    Script Date: 01/11/2023 21:15:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[AspNetRoleClaims](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[RoleId] [nvarchar](450) NOT NULL,
	[ClaimType] [nvarchar](max) NULL,
	[ClaimValue] [nvarchar](max) NULL,
 CONSTRAINT [PK_AspNetRoleClaims] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[AspNetRoles]    Script Date: 01/11/2023 21:15:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[AspNetRoles](
	[Id] [nvarchar](450) NOT NULL,
	[Name] [nvarchar](256) NULL,
	[NormalizedName] [nvarchar](256) NULL,
	[ConcurrencyStamp] [nvarchar](max) NULL,
 CONSTRAINT [PK_AspNetRoles] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[AspNetUserClaims]    Script Date: 01/11/2023 21:15:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[AspNetUserClaims](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[UserId] [nvarchar](450) NOT NULL,
	[ClaimType] [nvarchar](max) NULL,
	[ClaimValue] [nvarchar](max) NULL,
 CONSTRAINT [PK_AspNetUserClaims] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[AspNetUserLogins]    Script Date: 01/11/2023 21:15:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[AspNetUserLogins](
	[LoginProvider] [nvarchar](128) NOT NULL,
	[ProviderKey] [nvarchar](128) NOT NULL,
	[ProviderDisplayName] [nvarchar](max) NULL,
	[UserId] [nvarchar](450) NOT NULL,
 CONSTRAINT [PK_AspNetUserLogins] PRIMARY KEY CLUSTERED 
(
	[LoginProvider] ASC,
	[ProviderKey] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[AspNetUserRoles]    Script Date: 01/11/2023 21:15:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[AspNetUserRoles](
	[UserId] [nvarchar](450) NOT NULL,
	[RoleId] [nvarchar](450) NOT NULL,
 CONSTRAINT [PK_AspNetUserRoles] PRIMARY KEY CLUSTERED 
(
	[UserId] ASC,
	[RoleId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[AspNetUserTokens]    Script Date: 01/11/2023 21:15:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[AspNetUserTokens](
	[UserId] [nvarchar](450) NOT NULL,
	[LoginProvider] [nvarchar](128) NOT NULL,
	[Name] [nvarchar](128) NOT NULL,
	[Value] [nvarchar](max) NULL,
 CONSTRAINT [PK_AspNetUserTokens] PRIMARY KEY CLUSTERED 
(
	[UserId] ASC,
	[LoginProvider] ASC,
	[Name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[BIKE]    Script Date: 01/11/2023 21:15:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BIKE](
	[BikeId] [int] NOT NULL,
	[BikeName] [varchar](30) NULL,
	[LockStatus] [varchar](10) NULL,
 CONSTRAINT [XPKBIKE] PRIMARY KEY CLUSTERED 
(
	[BikeId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[BIKE_LOCK]    Script Date: 01/11/2023 21:15:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BIKE_LOCK](
	[LockId] [int] IDENTITY(1,1) NOT NULL,
	[LockTime] [datetime] NULL,
	[StationId] [int] NOT NULL,
	[TagId] [varchar](30) NOT NULL,
	[BikeId] [int] NOT NULL,
 CONSTRAINT [XPKBIKE_LOCK] PRIMARY KEY CLUSTERED 
(
	[LockId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[BIKE_STATION]    Script Date: 01/11/2023 21:15:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BIKE_STATION](
	[StationId] [int] NOT NULL,
	[StationName] [varchar](50) NULL,
	[Adress] [varchar](50) NULL,
	[PONumber] [int] NOT NULL,
 CONSTRAINT [XPKBIKE_STATION] PRIMARY KEY CLUSTERED 
(
	[StationId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[BIKE_UNLOCK]    Script Date: 01/11/2023 21:15:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BIKE_UNLOCK](
	[UnlockId] [int] IDENTITY(1,1) NOT NULL,
	[UnlockTime] [datetime] NULL,
	[StationId] [int] NOT NULL,
	[TagId] [varchar](30) NOT NULL,
	[BikeId] [int] NOT NULL,
 CONSTRAINT [XPKBIKE_UNLOCK] PRIMARY KEY CLUSTERED 
(
	[UnlockId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[MUNICIPALITY]    Script Date: 01/11/2023 21:15:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[MUNICIPALITY](
	[MunicipalityId] [int] NOT NULL,
	[MunicipalityName] [varchar](50) NULL,
 CONSTRAINT [XPKMUNICIPALITY] PRIMARY KEY CLUSTERED 
(
	[MunicipalityId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PO_LOCATION]    Script Date: 01/11/2023 21:15:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PO_LOCATION](
	[PONumber] [int] NOT NULL,
	[MunicipalityId] [int] NOT NULL,
 CONSTRAINT [XPKPO_LOCATION] PRIMARY KEY CLUSTERED 
(
	[PONumber] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
INSERT [dbo].[__EFMigrationsHistory] ([MigrationId], [ProductVersion]) VALUES (N'20231013223458_Initial Create', N'7.0.12')
GO
INSERT [dbo].[AspNetUsers] ([Id], [FirstName], [LastName], [UserName], [NormalizedUserName], [Email], [NormalizedEmail], [EmailConfirmed], [PasswordHash], [SecurityStamp], [ConcurrencyStamp], [PhoneNumber], [PhoneNumberConfirmed], [TwoFactorEnabled], [LockoutEnd], [LockoutEnabled], [AccessFailedCount]) VALUES (N'7d33d1b0-a56d-40ea-815a-6d5d82d703dc', N'Eva', N'Elliot', N'eva@gmail.com', N'EVA@GMAIL.COM', N'eva@gmail.com', N'EVA@GMAIL.COM', 0, N'AQAAAAIAAYagAAAAELjW8JUv3iU13yXrytYiao5f3O7aOk3n3fMQla3duOBCtOLDtlFCNJEwI3dXH5c5zA==', N'YXWCRIFI6EBVS4ILM5WM3KN4MTG7THVM', N'1b2bad29-6df5-4096-81a3-8b9681d6305d', NULL, 0, 0, NULL, 1, 0)
INSERT [dbo].[AspNetUsers] ([Id], [FirstName], [LastName], [UserName], [NormalizedUserName], [Email], [NormalizedEmail], [EmailConfirmed], [PasswordHash], [SecurityStamp], [ConcurrencyStamp], [PhoneNumber], [PhoneNumberConfirmed], [TwoFactorEnabled], [LockoutEnd], [LockoutEnabled], [AccessFailedCount]) VALUES (N'cfc02e7c-cffe-436a-b224-1a43b07dc47d', N'Adam', N'Adams', N'adam@gmail.com', N'ADAM@GMAIL.COM', N'adam@gmail.com', N'ADAM@GMAIL.COM', 0, N'AQAAAAIAAYagAAAAEJTLpnGN4HnBZAdUgNBwagQ2F1dhNDEtkHGooFfdq/D0UIG/+NaKaEmnCKrBFUp/7Q==', N'ZFF6OOU5CYPRWH42HE4B377ORBSDLLEF', N'35bc321c-3c73-45a7-a079-047f81d81b23', NULL, 0, 0, NULL, 1, 0)
INSERT [dbo].[AspNetUsers] ([Id], [FirstName], [LastName], [UserName], [NormalizedUserName], [Email], [NormalizedEmail], [EmailConfirmed], [PasswordHash], [SecurityStamp], [ConcurrencyStamp], [PhoneNumber], [PhoneNumberConfirmed], [TwoFactorEnabled], [LockoutEnd], [LockoutEnabled], [AccessFailedCount]) VALUES (N'd8f05bd3-febc-467a-88a1-303d85b5b9bd', N'James', N'May', N'james@topgear.com', N'JAMES@TOPGEAR.COM', N'james@topgear.com', N'JAMES@TOPGEAR.COM', 0, N'AQAAAAIAAYagAAAAEFmUMtRXzTDI5SaLNaQb//QzYQ+oIoO42QWoqOKShj+aOd09LQPeXciPPg9vkMKf6A==', N'KVBMFHZ5XH6GJ7TT4VHRDDCWB746QZ3Z', N'd241afd5-f5ab-4494-9f96-1f9b62c541c5', NULL, 0, 0, NULL, 1, 0)
GO
INSERT [dbo].[BIKE] ([BikeId], [BikeName], [LockStatus]) VALUES (1, N'Zelda', N'Locked')
INSERT [dbo].[BIKE] ([BikeId], [BikeName], [LockStatus]) VALUES (2, N'Link', N'Locked')
INSERT [dbo].[BIKE] ([BikeId], [BikeName], [LockStatus]) VALUES (3, N'Onox', N'Locked')
INSERT [dbo].[BIKE] ([BikeId], [BikeName], [LockStatus]) VALUES (4, N'Impa', N'Locked')
INSERT [dbo].[BIKE] ([BikeId], [BikeName], [LockStatus]) VALUES (5, N'Malon', N'Locked')
INSERT [dbo].[BIKE] ([BikeId], [BikeName], [LockStatus]) VALUES (6, N'Kafei', N'Locked')
INSERT [dbo].[BIKE] ([BikeId], [BikeName], [LockStatus]) VALUES (7, N'Kaepora', N'Locked')
INSERT [dbo].[BIKE] ([BikeId], [BikeName], [LockStatus]) VALUES (8, N'Gaebora', N'Unlocked')
INSERT [dbo].[BIKE] ([BikeId], [BikeName], [LockStatus]) VALUES (9, N'Midna', N'Locked')
GO
SET IDENTITY_INSERT [dbo].[BIKE_LOCK] ON 

INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (7, CAST(N'2023-10-03T00:34:55.723' AS DateTime), 1, N'E2B0E91B', 1)
INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (8, CAST(N'2023-10-03T00:35:31.470' AS DateTime), 1, N'E2B0E91B', 1)
INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (9, CAST(N'2023-10-03T00:38:37.237' AS DateTime), 1, N'24243885', 1)
INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (10, CAST(N'2023-10-14T15:54:44.010' AS DateTime), 2, N'142E37CF', 1)
INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (11, CAST(N'2023-10-29T02:00:31.067' AS DateTime), 2, N'142E37CF', 1)
INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (12, CAST(N'2023-10-29T02:03:05.373' AS DateTime), 1, N'142E37CF', 1)
INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (13, CAST(N'2023-10-29T02:05:27.600' AS DateTime), 5, N'142E37CF', 9)
INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (14, CAST(N'2023-10-29T02:07:07.017' AS DateTime), 3, N'E2B0E91B', 9)
INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (15, CAST(N'2023-10-29T02:07:27.703' AS DateTime), 4, N'142E37CF', 9)
INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (16, CAST(N'2023-10-29T02:08:02.367' AS DateTime), 2, N'E2B0E91B', 8)
INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (17, CAST(N'2023-10-29T02:11:53.227' AS DateTime), 4, N'E2B0E91B', 3)
INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (18, CAST(N'2023-10-29T02:12:11.743' AS DateTime), 4, N'142E37CF', 6)
INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (19, CAST(N'2023-10-29T02:18:32.210' AS DateTime), 3, N'E2B0E91B', 5)
INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (20, CAST(N'2023-10-29T06:22:27.230' AS DateTime), 5, N'B461BE57', 2)
INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (21, CAST(N'2023-10-29T06:23:50.270' AS DateTime), 3, N'B461BE57', 4)
INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (22, CAST(N'2023-10-29T06:25:04.220' AS DateTime), 2, N'B461BE57', 7)
INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (23, CAST(N'2023-10-29T06:25:29.993' AS DateTime), 4, N'B461BE57', 2)
INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (24, CAST(N'2023-10-29T19:58:32.243' AS DateTime), 5, N'B461BE57', 2)
INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (25, CAST(N'2023-11-01T00:22:43.137' AS DateTime), 4, N'E2B0E91B', 2)
INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (26, CAST(N'2023-11-01T00:24:02.903' AS DateTime), 5, N'E2B0E91B', 2)
INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (27, CAST(N'2023-11-01T19:04:57.643' AS DateTime), 3, N'142E37CF', 8)
INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (30, CAST(N'2023-11-01T20:03:10.850' AS DateTime), 1, N'4A590D47', 3)
INSERT [dbo].[BIKE_LOCK] ([LockId], [LockTime], [StationId], [TagId], [BikeId]) VALUES (31, CAST(N'2023-11-01T20:03:28.360' AS DateTime), 2, N'4A590D47', 5)
SET IDENTITY_INSERT [dbo].[BIKE_LOCK] OFF
GO
INSERT [dbo].[BIKE_STATION] ([StationId], [StationName], [Adress], [PONumber]) VALUES (1, N'USN Nord', N'Kjølnes Ring 58', 3922)
INSERT [dbo].[BIKE_STATION] ([StationId], [StationName], [Adress], [PONumber]) VALUES (2, N'Jotunvegen', N'Jotunvegen 38', 3913)
INSERT [dbo].[BIKE_STATION] ([StationId], [StationName], [Adress], [PONumber]) VALUES (3, N'Porselensfabrikken', N'Drangedalsvegen 2', 3920)
INSERT [dbo].[BIKE_STATION] ([StationId], [StationName], [Adress], [PONumber]) VALUES (4, N'Down Town', N'Kulltangvegen 70', 3921)
INSERT [dbo].[BIKE_STATION] ([StationId], [StationName], [Adress], [PONumber]) VALUES (5, N'Hovenga Senteret', N'Augestadvegen 3', 3914)
GO
SET IDENTITY_INSERT [dbo].[BIKE_UNLOCK] ON 

INSERT [dbo].[BIKE_UNLOCK] ([UnlockId], [UnlockTime], [StationId], [TagId], [BikeId]) VALUES (3, CAST(N'2023-10-03T00:35:35.797' AS DateTime), 1, N'E2B0E91B', 1)
INSERT [dbo].[BIKE_UNLOCK] ([UnlockId], [UnlockTime], [StationId], [TagId], [BikeId]) VALUES (4, CAST(N'2023-10-14T15:54:34.660' AS DateTime), 2, N'142E37CF', 1)
INSERT [dbo].[BIKE_UNLOCK] ([UnlockId], [UnlockTime], [StationId], [TagId], [BikeId]) VALUES (8, CAST(N'2023-10-29T01:59:48.687' AS DateTime), 2, N'142E37CF', 1)
INSERT [dbo].[BIKE_UNLOCK] ([UnlockId], [UnlockTime], [StationId], [TagId], [BikeId]) VALUES (9, CAST(N'2023-10-29T02:02:55.213' AS DateTime), 2, N'142E37CF', 1)
INSERT [dbo].[BIKE_UNLOCK] ([UnlockId], [UnlockTime], [StationId], [TagId], [BikeId]) VALUES (10, CAST(N'2023-10-29T02:05:16.813' AS DateTime), 1, N'142E37CF', 9)
INSERT [dbo].[BIKE_UNLOCK] ([UnlockId], [UnlockTime], [StationId], [TagId], [BikeId]) VALUES (11, CAST(N'2023-10-29T02:06:48.353' AS DateTime), 5, N'E2B0E91B', 9)
INSERT [dbo].[BIKE_UNLOCK] ([UnlockId], [UnlockTime], [StationId], [TagId], [BikeId]) VALUES (12, CAST(N'2023-10-29T02:07:18.137' AS DateTime), 3, N'142E37CF', 9)
INSERT [dbo].[BIKE_UNLOCK] ([UnlockId], [UnlockTime], [StationId], [TagId], [BikeId]) VALUES (13, CAST(N'2023-10-29T02:07:53.797' AS DateTime), 1, N'E2B0E91B', 8)
INSERT [dbo].[BIKE_UNLOCK] ([UnlockId], [UnlockTime], [StationId], [TagId], [BikeId]) VALUES (14, CAST(N'2023-10-29T02:11:46.003' AS DateTime), 1, N'E2B0E91B', 3)
INSERT [dbo].[BIKE_UNLOCK] ([UnlockId], [UnlockTime], [StationId], [TagId], [BikeId]) VALUES (15, CAST(N'2023-10-29T02:12:03.020' AS DateTime), 1, N'142E37CF', 6)
INSERT [dbo].[BIKE_UNLOCK] ([UnlockId], [UnlockTime], [StationId], [TagId], [BikeId]) VALUES (16, CAST(N'2023-10-29T02:18:19.180' AS DateTime), 1, N'E2B0E91B', 5)
INSERT [dbo].[BIKE_UNLOCK] ([UnlockId], [UnlockTime], [StationId], [TagId], [BikeId]) VALUES (17, CAST(N'2023-10-29T06:21:21.670' AS DateTime), 1, N'B461BE57', 2)
INSERT [dbo].[BIKE_UNLOCK] ([UnlockId], [UnlockTime], [StationId], [TagId], [BikeId]) VALUES (18, CAST(N'2023-10-29T06:23:10.750' AS DateTime), 1, N'B461BE57', 4)
INSERT [dbo].[BIKE_UNLOCK] ([UnlockId], [UnlockTime], [StationId], [TagId], [BikeId]) VALUES (19, CAST(N'2023-10-29T06:24:54.720' AS DateTime), 1, N'B461BE57', 7)
INSERT [dbo].[BIKE_UNLOCK] ([UnlockId], [UnlockTime], [StationId], [TagId], [BikeId]) VALUES (20, CAST(N'2023-10-29T06:25:12.813' AS DateTime), 5, N'B461BE57', 2)
INSERT [dbo].[BIKE_UNLOCK] ([UnlockId], [UnlockTime], [StationId], [TagId], [BikeId]) VALUES (21, CAST(N'2023-10-29T19:58:18.510' AS DateTime), 4, N'B461BE57', 2)
INSERT [dbo].[BIKE_UNLOCK] ([UnlockId], [UnlockTime], [StationId], [TagId], [BikeId]) VALUES (22, CAST(N'2023-11-01T00:21:51.960' AS DateTime), 5, N'E2B0E91B', 2)
INSERT [dbo].[BIKE_UNLOCK] ([UnlockId], [UnlockTime], [StationId], [TagId], [BikeId]) VALUES (23, CAST(N'2023-11-01T00:23:48.850' AS DateTime), 4, N'E2B0E91B', 2)
INSERT [dbo].[BIKE_UNLOCK] ([UnlockId], [UnlockTime], [StationId], [TagId], [BikeId]) VALUES (24, CAST(N'2023-11-01T19:04:43.887' AS DateTime), 2, N'142E37CF', 8)
INSERT [dbo].[BIKE_UNLOCK] ([UnlockId], [UnlockTime], [StationId], [TagId], [BikeId]) VALUES (27, CAST(N'2023-11-01T19:06:22.873' AS DateTime), 5, N'142E37CF', 8)
INSERT [dbo].[BIKE_UNLOCK] ([UnlockId], [UnlockTime], [StationId], [TagId], [BikeId]) VALUES (28, CAST(N'2023-11-01T20:02:41.970' AS DateTime), 4, N'4A590D47', 3)
INSERT [dbo].[BIKE_UNLOCK] ([UnlockId], [UnlockTime], [StationId], [TagId], [BikeId]) VALUES (29, CAST(N'2023-11-01T20:03:20.900' AS DateTime), 3, N'4A590D47', 5)
SET IDENTITY_INSERT [dbo].[BIKE_UNLOCK] OFF
GO
INSERT [dbo].[MUNICIPALITY] ([MunicipalityId], [MunicipalityName]) VALUES (3806, N'Porsgrunn')
INSERT [dbo].[MUNICIPALITY] ([MunicipalityId], [MunicipalityName]) VALUES (3807, N'Skien')
GO
INSERT [dbo].[PO_LOCATION] ([PONumber], [MunicipalityId]) VALUES (3913, 3806)
INSERT [dbo].[PO_LOCATION] ([PONumber], [MunicipalityId]) VALUES (3914, 3806)
INSERT [dbo].[PO_LOCATION] ([PONumber], [MunicipalityId]) VALUES (3920, 3806)
INSERT [dbo].[PO_LOCATION] ([PONumber], [MunicipalityId]) VALUES (3921, 3806)
INSERT [dbo].[PO_LOCATION] ([PONumber], [MunicipalityId]) VALUES (3922, 3806)
GO
INSERT [dbo].[TAG] ([TagId], [TagColor], [TagText]) VALUES (N'142E37CF', N'black', N'Svart')
INSERT [dbo].[TAG] ([TagId], [TagColor], [TagText]) VALUES (N'24243885', N'blue', N'Blå')
INSERT [dbo].[TAG] ([TagId], [TagColor], [TagText]) VALUES (N'4A590D47', N'red', N'Rød')
INSERT [dbo].[TAG] ([TagId], [TagColor], [TagText]) VALUES (N'B461BE57', N'green', N'Grønn')
INSERT [dbo].[TAG] ([TagId], [TagColor], [TagText]) VALUES (N'E2B0E91B', N'yellow', N'Gul')
GO
SET IDENTITY_INSERT [dbo].[USER_TAG] ON 

INSERT [dbo].[USER_TAG] ([Id], [UserId], [UserKey]) VALUES (8, N'cfc02e7c-cffe-436a-b224-1a43b07dc47d', N'B461BE57')
INSERT [dbo].[USER_TAG] ([Id], [UserId], [UserKey]) VALUES (10, N'7d33d1b0-a56d-40ea-815a-6d5d82d703dc', N'E2B0E91B')
INSERT [dbo].[USER_TAG] ([Id], [UserId], [UserKey]) VALUES (11, N'd8f05bd3-febc-467a-88a1-303d85b5b9bd', N'4A590D47')
SET IDENTITY_INSERT [dbo].[USER_TAG] OFF
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [UQ__USER_TAG__1788CC4D4BFBD321]    Script Date: 01/11/2023 21:15:39 ******/
ALTER TABLE [dbo].[USER_TAG] ADD UNIQUE NONCLUSTERED 
(
	[UserId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [UQ__USER_TAG__296ADCF02A1042E8]    Script Date: 01/11/2023 21:15:39 ******/
ALTER TABLE [dbo].[USER_TAG] ADD UNIQUE NONCLUSTERED 
(
	[UserKey] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[AspNetRoleClaims]  WITH CHECK ADD  CONSTRAINT [FK_AspNetRoleClaims_AspNetRoles_RoleId] FOREIGN KEY([RoleId])
REFERENCES [dbo].[AspNetRoles] ([Id])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[AspNetRoleClaims] CHECK CONSTRAINT [FK_AspNetRoleClaims_AspNetRoles_RoleId]
GO
ALTER TABLE [dbo].[AspNetUserClaims]  WITH CHECK ADD  CONSTRAINT [FK_AspNetUserClaims_AspNetUsers_UserId] FOREIGN KEY([UserId])
REFERENCES [dbo].[AspNetUsers] ([Id])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[AspNetUserClaims] CHECK CONSTRAINT [FK_AspNetUserClaims_AspNetUsers_UserId]
GO
ALTER TABLE [dbo].[AspNetUserLogins]  WITH CHECK ADD  CONSTRAINT [FK_AspNetUserLogins_AspNetUsers_UserId] FOREIGN KEY([UserId])
REFERENCES [dbo].[AspNetUsers] ([Id])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[AspNetUserLogins] CHECK CONSTRAINT [FK_AspNetUserLogins_AspNetUsers_UserId]
GO
ALTER TABLE [dbo].[AspNetUserRoles]  WITH CHECK ADD  CONSTRAINT [FK_AspNetUserRoles_AspNetRoles_RoleId] FOREIGN KEY([RoleId])
REFERENCES [dbo].[AspNetRoles] ([Id])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[AspNetUserRoles] CHECK CONSTRAINT [FK_AspNetUserRoles_AspNetRoles_RoleId]
GO
ALTER TABLE [dbo].[AspNetUserRoles]  WITH CHECK ADD  CONSTRAINT [FK_AspNetUserRoles_AspNetUsers_UserId] FOREIGN KEY([UserId])
REFERENCES [dbo].[AspNetUsers] ([Id])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[AspNetUserRoles] CHECK CONSTRAINT [FK_AspNetUserRoles_AspNetUsers_UserId]
GO
ALTER TABLE [dbo].[AspNetUserTokens]  WITH CHECK ADD  CONSTRAINT [FK_AspNetUserTokens_AspNetUsers_UserId] FOREIGN KEY([UserId])
REFERENCES [dbo].[AspNetUsers] ([Id])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[AspNetUserTokens] CHECK CONSTRAINT [FK_AspNetUserTokens_AspNetUsers_UserId]
GO
ALTER TABLE [dbo].[BIKE_LOCK]  WITH CHECK ADD  CONSTRAINT [R_15] FOREIGN KEY([BikeId])
REFERENCES [dbo].[BIKE] ([BikeId])
GO
ALTER TABLE [dbo].[BIKE_LOCK] CHECK CONSTRAINT [R_15]
GO
ALTER TABLE [dbo].[BIKE_LOCK]  WITH CHECK ADD  CONSTRAINT [R_16] FOREIGN KEY([TagId])
REFERENCES [dbo].[TAG] ([TagId])
GO
ALTER TABLE [dbo].[BIKE_LOCK] CHECK CONSTRAINT [R_16]
GO
ALTER TABLE [dbo].[BIKE_LOCK]  WITH CHECK ADD  CONSTRAINT [R_17] FOREIGN KEY([StationId])
REFERENCES [dbo].[BIKE_STATION] ([StationId])
GO
ALTER TABLE [dbo].[BIKE_LOCK] CHECK CONSTRAINT [R_17]
GO
ALTER TABLE [dbo].[BIKE_STATION]  WITH CHECK ADD  CONSTRAINT [R_10] FOREIGN KEY([PONumber])
REFERENCES [dbo].[PO_LOCATION] ([PONumber])
GO
ALTER TABLE [dbo].[BIKE_STATION] CHECK CONSTRAINT [R_10]
GO
ALTER TABLE [dbo].[BIKE_UNLOCK]  WITH CHECK ADD  CONSTRAINT [R_11] FOREIGN KEY([StationId])
REFERENCES [dbo].[BIKE_STATION] ([StationId])
GO
ALTER TABLE [dbo].[BIKE_UNLOCK] CHECK CONSTRAINT [R_11]
GO
ALTER TABLE [dbo].[BIKE_UNLOCK]  WITH CHECK ADD  CONSTRAINT [R_13] FOREIGN KEY([TagId])
REFERENCES [dbo].[TAG] ([TagId])
GO
ALTER TABLE [dbo].[BIKE_UNLOCK] CHECK CONSTRAINT [R_13]
GO
ALTER TABLE [dbo].[BIKE_UNLOCK]  WITH CHECK ADD  CONSTRAINT [R_14] FOREIGN KEY([BikeId])
REFERENCES [dbo].[BIKE] ([BikeId])
GO
ALTER TABLE [dbo].[BIKE_UNLOCK] CHECK CONSTRAINT [R_14]
GO
ALTER TABLE [dbo].[PO_LOCATION]  WITH CHECK ADD  CONSTRAINT [R_9] FOREIGN KEY([MunicipalityId])
REFERENCES [dbo].[MUNICIPALITY] ([MunicipalityId])
GO
ALTER TABLE [dbo].[PO_LOCATION] CHECK CONSTRAINT [R_9]
GO
ALTER TABLE [dbo].[USER_TAG]  WITH CHECK ADD  CONSTRAINT [FK_USER_TAG_TAG] FOREIGN KEY([UserKey])
REFERENCES [dbo].[TAG] ([TagId])
GO
ALTER TABLE [dbo].[USER_TAG] CHECK CONSTRAINT [FK_USER_TAG_TAG]
GO
ALTER TABLE [dbo].[USER_TAG]  WITH CHECK ADD  CONSTRAINT [FK_USER_TAG_USER] FOREIGN KEY([UserId])
REFERENCES [dbo].[AspNetUsers] ([Id])
GO
ALTER TABLE [dbo].[USER_TAG] CHECK CONSTRAINT [FK_USER_TAG_USER]
GO
/****** Object:  StoredProcedure [dbo].[DeleteTag]    Script Date: 01/11/2023 21:15:39 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[DeleteTag] @tagId VARCHAR(30) AS
DELETE FROM USER_TAG WHERE UserKey = @tagId
DELETE FROM BIKE_UNLOCK WHERE TagId = @tagId
DELETE FROM BIKE_LOCK WHERE TagId = @tagId
DELETE FROM TAG WHERE TagId = @tagId
GO
/****** Object:  StoredProcedure [dbo].[GetBikeUnlocks]    Script Date: 01/11/2023 21:15:39 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[GetBikeUnlocks] @tagId VARCHAR(30) AS
SELECT BU.UnlockTime, BS.StationName, BIKE.BikeName
FROM BIKE_UNLOCK AS BU, BIKE, BIKE_STATION AS BS
WHERE BIKE.BikeId = BU.BikeId
AND BS.StationId = BU.StationId
AND BU.TagId = @tagId
ORDER BY BU.UnlockTime DESC
GO
/****** Object:  StoredProcedure [dbo].[InsertLock]    Script Date: 01/11/2023 21:15:39 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[InsertLock] @stationId int, @tagId VARCHAR(30), @bikeId int AS
INSERT INTO BIKE_LOCK 
VALUES (GETDATE(), @stationId, @tagId, @bikeId)
GO
/****** Object:  StoredProcedure [dbo].[InsertTag]    Script Date: 01/11/2023 21:15:39 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[InsertTag] @tagId VARCHAR(30), @tagColor VARCHAR(30), @tagText VARCHAR(30) AS
INSERT INTO TAG
VALUES (@tagId, @tagColor, @tagText)
GO
/****** Object:  StoredProcedure [dbo].[InsertUnlock]    Script Date: 01/11/2023 21:15:39 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[InsertUnlock] @stationId int, @tagId VARCHAR(30), @bikeId int AS
INSERT INTO BIKE_UNLOCK 
VALUES (GETDATE(), @stationId, @tagId, @bikeId)
GO
/****** Object:  StoredProcedure [dbo].[InsertUserTag]    Script Date: 01/11/2023 21:15:39 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[InsertUserTag] @userId nvarchar(450), @userKey VARCHAR(30) AS
INSERT INTO USER_TAG
VALUES (@userId, @userKey)
GO
/****** Object:  StoredProcedure [dbo].[UpdateLock]    Script Date: 01/11/2023 21:15:39 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[UpdateLock] @bikeId int, @lockStatus VARCHAR(10) AS
UPDATE BIKE
SET LockStatus = @lockStatus
WHERE BikeId LIKE @bikeId
GO
