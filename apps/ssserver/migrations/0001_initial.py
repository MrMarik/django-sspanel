# Generated by Django 2.0.5 on 2018-06-18 21:17

import apps.utils
import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="AliveIp",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("node_id", models.IntegerField(verbose_name="节点id")),
                ("ip", models.CharField(max_length=128, verbose_name="设备ip")),
                ("user", models.CharField(max_length=128, verbose_name="用户名")),
                ("log_time", models.DateTimeField(auto_now=True, verbose_name="日志时间")),
            ],
            options={"verbose_name_plural": "节点在线IP", "ordering": ["-log_time"]},
        ),
        migrations.CreateModel(
            name="Node",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("node_id", models.IntegerField(unique=True, verbose_name="节点id")),
                (
                    "port",
                    models.IntegerField(
                        blank=True,
                        help_text="单端口多用户时需要",
                        null=True,
                        verbose_name="节点端口",
                    ),
                ),
                (
                    "password",
                    models.CharField(
                        default="password",
                        help_text="单端口多用户时需要",
                        max_length=32,
                        verbose_name="节点密码",
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        choices=[
                            ("AF", "阿富汗"),
                            ("AX", "奥兰群岛"),
                            ("AL", "阿尔巴尼亚"),
                            ("DZ", "阿尔及利亚"),
                            ("AS", "美属萨摩亚"),
                            ("AD", "安道尔"),
                            ("AO", "安哥拉"),
                            ("AI", "安圭拉"),
                            ("AQ", "南极洲"),
                            ("AG", "安提瓜和巴布达"),
                            ("AR", "阿根廷"),
                            ("AM", "亚美尼亚"),
                            ("AW", "阿鲁巴"),
                            ("AU", "澳大利亚"),
                            ("AT", "奥地利"),
                            ("AZ", "阿塞拜疆"),
                            ("BS", "巴哈马"),
                            ("BH", "巴林"),
                            ("BD", "孟加拉国"),
                            ("BB", "巴巴多斯"),
                            ("BY", "白俄罗斯"),
                            ("BE", "比利时"),
                            ("BZ", "伯利兹"),
                            ("BJ", "贝宁"),
                            ("BM", "百慕大"),
                            ("BT", "不丹"),
                            ("BO", "玻利维亚（多民族国）"),
                            ("BA", "波斯尼亚和黑塞哥维那"),
                            ("BW", "博茨瓦纳"),
                            ("BV", "布维岛"),
                            ("BR", "巴西"),
                            ("IO", "英属印度洋领地"),
                            ("BN", "文莱达鲁萨兰国"),
                            ("BG", "保加利亚"),
                            ("BF", "布基纳法索"),
                            ("BI", "布隆迪"),
                            ("CV", "Cabo Verde"),
                            ("KH", "柬埔寨"),
                            ("CM", "喀麦隆"),
                            ("CA", "加拿大"),
                            ("KY", "开曼群岛"),
                            ("CF", "中非共和国"),
                            ("TD", "乍得"),
                            ("CL", "智利"),
                            ("CN", "中国"),
                            ("CX", "圣诞岛"),
                            ("CC", "科科斯（基林）群岛"),
                            ("CO", "哥伦比亚"),
                            ("KM", "科摩罗"),
                            ("CD", "刚果（该民主共和国）"),
                            ("CG", "刚果"),
                            ("CK", "库克群岛"),
                            ("CR", "哥斯达黎加"),
                            ("CI", "科特迪瓦"),
                            ("HR", "克罗地亚"),
                            ("CU", "古巴"),
                            ("CW", "库拉索"),
                            ("CY", "塞浦路斯"),
                            ("CZ", "捷克"),
                            ("DK", "丹麦"),
                            ("DJ", "吉布提"),
                            ("DM", "多米尼克"),
                            ("DO", "多米尼加共和国"),
                            ("EC", "厄瓜多尔"),
                            ("EG", "埃及"),
                            ("SV", "萨尔瓦多"),
                            ("GQ", "赤道几内亚"),
                            ("ER", "厄立特里亚"),
                            ("EE", "爱沙尼亚"),
                            ("ET", "埃塞俄比亚"),
                            ("FK", "福克兰群岛[马尔维纳斯]"),
                            ("FO", "法罗群岛"),
                            ("FJ", "斐济"),
                            ("FI", "芬兰"),
                            ("FR", "法国"),
                            ("GF", "法属圭亚那"),
                            ("PF", "法属波利尼西亚"),
                            ("TF", "法国南部领土"),
                            ("GA", "加蓬"),
                            ("GM", "冈比亚"),
                            ("GE", "格鲁吉亚"),
                            ("DE", "德国"),
                            ("GH", "加纳"),
                            ("GI", "直布罗陀"),
                            ("GR", "希腊"),
                            ("GL", "格陵兰"),
                            ("GD", "格林纳达"),
                            ("GP", "Guadeloupe"),
                            ("GU", "关岛"),
                            ("GT", "危地马拉"),
                            ("GG", "根西岛"),
                            ("GN", "几内亚"),
                            ("GW", "几内亚比绍"),
                            ("GY", "圭亚那"),
                            ("HT", "海地"),
                            ("HM", "赫德岛和麦克唐纳群岛"),
                            ("VA", "罗马教廷"),
                            ("HN", "洪都拉斯"),
                            ("HK", "香港"),
                            ("HU", "匈牙利"),
                            ("IS", "冰岛"),
                            ("ID", "印度尼西亚"),
                            ("IR", "伊朗（伊斯兰共和国）"),
                            ("IQ", "伊拉克"),
                            ("IE", "爱尔兰"),
                            ("IM", "马恩岛"),
                            ("IL", "以色列"),
                            ("IT", "意大利"),
                            ("JM", "牙买加"),
                            ("JP", "日本"),
                            ("JE", "泽西岛"),
                            ("JO", "约旦"),
                            ("KZ", "哈萨克斯坦"),
                            ("KE", "肯尼亚"),
                            ("KI", "基里巴斯"),
                            ("KP", "韩国（朝鲜民主主义人民共和国）"),
                            ("KR", "韩国（共和国）"),
                            ("KW", "科威特"),
                            ("KG", "吉尔吉斯斯坦"),
                            ("LA", "老挝人民民主共和国"),
                            ("LV", "拉脱维亚"),
                            ("LB", "黎巴嫩"),
                            ("LS", "莱索托"),
                            ("LR", "利比里亚"),
                            ("LY", "利比亚"),
                            ("LI", "列支敦士登"),
                            ("LT", "立陶宛"),
                            ("LU", "卢森堡"),
                            ("MO", "澳门"),
                            ("MK", "马其顿（前南斯拉夫共和国）"),
                            ("MG", "马达加斯加"),
                            ("MW", "马拉维"),
                            ("MY", "马来西亚"),
                            ("MV", "马尔代夫"),
                            ("ML", "Mali"),
                            ("MT", "马耳他"),
                            ("MH", "马绍尔群岛"),
                            ("MQ", "马提尼克岛"),
                            ("MR", "毛里塔尼亚"),
                            ("MU", "毛里求斯"),
                            ("YT", "马约特岛"),
                            ("MX", "墨西哥"),
                            ("FM", "密克罗尼西亚联邦"),
                            ("MD", "摩尔多瓦共和国"),
                            ("MC", "摩纳哥"),
                            ("MN", "蒙古"),
                            ("ME", "黑山"),
                            ("MS", "蒙特塞拉特"),
                            ("MA", "摩洛哥"),
                            ("MZ", "莫桑比克"),
                            ("MM", "缅甸"),
                            ("NA", "纳米比亚"),
                            ("NR", "瑙鲁"),
                            ("NP", "尼泊尔"),
                            ("NL", "荷兰"),
                            ("NC", "新喀里多尼亚"),
                            ("NZ", "新西兰"),
                            ("NI", "尼加拉瓜"),
                            ("NE", "尼日尔"),
                            ("NG", "尼日利亚"),
                            ("NU", "纽埃"),
                            ("NF", "诺福克岛"),
                            ("MP", "北马里亚纳群岛"),
                            ("NO", "挪威"),
                            ("OM", "阿曼"),
                            ("PK", "巴基斯坦"),
                            ("PW", "帕劳"),
                            ("PS", "巴勒斯坦，国家"),
                            ("PA", "巴拿马"),
                            ("PG", "巴布亚新几内亚"),
                            ("PY", "巴拉圭"),
                            ("PE", "秘鲁"),
                            ("PH", "菲律宾"),
                            ("PN", "皮特凯恩"),
                            ("PL", "波兰"),
                            ("PT", "葡萄牙"),
                            ("PR", "波多黎各"),
                            ("QA", "卡塔尔"),
                            ("RE", "留尼汪"),
                            ("RO", "罗马尼亚"),
                            ("RU", "俄罗斯联邦"),
                            ("RW", "卢旺达"),
                            ("BL", "圣巴泰勒米"),
                            ("SH", "圣赫勒拿，阿森松和特里斯坦达库尼亚"),
                            ("KN", "圣基茨和尼维斯"),
                        ],
                        default="CN",
                        max_length=2,
                        verbose_name="国家",
                    ),
                ),
                (
                    "custom_method",
                    models.SmallIntegerField(
                        choices=[(0, "否"), (1, "是")], default=0, verbose_name="自定义加密"
                    ),
                ),
                (
                    "show",
                    models.SmallIntegerField(
                        choices=[(1, "显示"), (-1, "不显示")], default=1, verbose_name="是否显示"
                    ),
                ),
                (
                    "node_type",
                    models.SmallIntegerField(
                        choices=[(0, "多端口多用户"), (1, "单端口多用户")],
                        default=0,
                        verbose_name="节点类型",
                    ),
                ),
                ("name", models.CharField(max_length=32, verbose_name="名字")),
                (
                    "info",
                    models.CharField(
                        blank=True, max_length=1024, null=True, verbose_name="节点说明"
                    ),
                ),
                ("server", models.CharField(max_length=128, verbose_name="服务器IP")),
                (
                    "method",
                    models.CharField(
                        choices=[
                            ("aes-256-cfb", "aes-256-cfb"),
                            ("aes-128-ctr", "aes-128-ctr"),
                            ("rc4-md5", "rc4-md5"),
                            ("salsa20", "salsa20"),
                            ("chacha20", "chacha20"),
                            ("none", "none"),
                        ],
                        default="aes-128-ctr",
                        max_length=32,
                        verbose_name="加密类型",
                    ),
                ),
                ("traffic_rate", models.FloatField(default=1.0, verbose_name="流量比例")),
                (
                    "protocol",
                    models.CharField(
                        choices=[
                            ("auth_sha1_v4", "auth_sha1_v4"),
                            ("auth_aes128_md5", "auth_aes128_md5"),
                            ("auth_aes128_sha1", "auth_aes128_sha1"),
                            ("auth_chain_a", "auth_chain_a"),
                            ("origin", "origin"),
                        ],
                        default="auth_chain_a",
                        max_length=32,
                        verbose_name="协议",
                    ),
                ),
                (
                    "protocol_param",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="协议参数"
                    ),
                ),
                (
                    "obfs",
                    models.CharField(
                        choices=[
                            ("plain", "plain"),
                            ("http_simple", "http_simple"),
                            ("http_simple_compatible", "http_simple_compatible"),
                            ("http_post", "http_post"),
                            ("tls1.2_ticket_auth", "tls1.2_ticket_auth"),
                        ],
                        default="http_simple",
                        max_length=32,
                        verbose_name="混淆",
                    ),
                ),
                (
                    "obfs_param",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=128,
                        null=True,
                        verbose_name="混淆参数",
                    ),
                ),
                (
                    "level",
                    models.PositiveIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MaxValueValidator(9),
                            django.core.validators.MinValueValidator(0),
                        ],
                        verbose_name="节点等级",
                    ),
                ),
                (
                    "total_traffic",
                    models.BigIntegerField(default=1073741824, verbose_name="总流量"),
                ),
                (
                    "human_total_traffic",
                    models.CharField(
                        blank=True,
                        default="1GB",
                        max_length=255,
                        null=True,
                        verbose_name="节点总流量",
                    ),
                ),
                (
                    "used_traffic",
                    models.BigIntegerField(default=0, verbose_name="已用流量"),
                ),
                (
                    "human_used_traffic",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="已用流量"
                    ),
                ),
                (
                    "order",
                    models.PositiveSmallIntegerField(default=1, verbose_name="排序"),
                ),
                (
                    "group",
                    models.CharField(default="谜之屋", max_length=32, verbose_name="分组名"),
                ),
            ],
            options={
                "verbose_name_plural": "节点",
                "db_table": "ss_node",
                "ordering": ["-show", "order"],
            },
        ),
        migrations.CreateModel(
            name="NodeInfoLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("node_id", models.IntegerField(verbose_name="节点id")),
                ("uptime", models.FloatField(verbose_name="更新时间")),
                ("load", models.CharField(max_length=32, verbose_name="负载")),
                ("log_time", models.IntegerField(verbose_name="日志时间")),
            ],
            options={
                "verbose_name_plural": "节点日志",
                "db_table": "ss_node_info_log",
                "ordering": ("-log_time",),
            },
        ),
        migrations.CreateModel(
            name="NodeOnlineLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("node_id", models.IntegerField(verbose_name="节点id")),
                ("online_user", models.IntegerField(verbose_name="在线人数")),
                ("log_time", models.IntegerField(verbose_name="日志时间")),
            ],
            options={"verbose_name_plural": "节点在线记录", "db_table": "ss_node_online_log"},
        ),
        migrations.CreateModel(
            name="SSUser",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_check_in_time",
                    models.DateTimeField(
                        default=datetime.datetime(1970, 1, 1, 8, 0),
                        editable=False,
                        null=True,
                        verbose_name="最后签到时间",
                    ),
                ),
                (
                    "password",
                    models.CharField(
                        db_column="passwd",
                        default=apps.utils.get_short_random_string,
                        max_length=32,
                        validators=[django.core.validators.MinLengthValidator(6)],
                        verbose_name="sspanel密码",
                    ),
                ),
                (
                    "port",
                    models.IntegerField(
                        db_column="port", unique=True, verbose_name="端口"
                    ),
                ),
                (
                    "last_use_time",
                    models.IntegerField(
                        db_column="t",
                        default=0,
                        editable=False,
                        help_text="时间戳",
                        verbose_name="最后使用时间",
                    ),
                ),
                (
                    "upload_traffic",
                    models.BigIntegerField(
                        db_column="u", default=0, verbose_name="上传流量"
                    ),
                ),
                (
                    "download_traffic",
                    models.BigIntegerField(
                        db_column="d", default=0, verbose_name="下载流量"
                    ),
                ),
                (
                    "transfer_enable",
                    models.BigIntegerField(
                        db_column="transfer_enable",
                        default=5368709120,
                        verbose_name="总流量",
                    ),
                ),
                (
                    "switch",
                    models.BooleanField(
                        db_column="switch", default=True, verbose_name="保留字段switch"
                    ),
                ),
                (
                    "enable",
                    models.BooleanField(
                        db_column="enable", default=True, verbose_name="开启与否"
                    ),
                ),
                (
                    "method",
                    models.CharField(
                        choices=[
                            ("aes-256-cfb", "aes-256-cfb"),
                            ("aes-128-ctr", "aes-128-ctr"),
                            ("rc4-md5", "rc4-md5"),
                            ("salsa20", "salsa20"),
                            ("chacha20", "chacha20"),
                            ("none", "none"),
                        ],
                        default="aes-128-ctr",
                        max_length=32,
                        verbose_name="加密类型",
                    ),
                ),
                (
                    "protocol",
                    models.CharField(
                        choices=[
                            ("auth_sha1_v4", "auth_sha1_v4"),
                            ("auth_aes128_md5", "auth_aes128_md5"),
                            ("auth_aes128_sha1", "auth_aes128_sha1"),
                            ("auth_chain_a", "auth_chain_a"),
                            ("origin", "origin"),
                        ],
                        default="auth_chain_a",
                        max_length=32,
                        verbose_name="协议",
                    ),
                ),
                (
                    "protocol_param",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="协议参数"
                    ),
                ),
                (
                    "obfs",
                    models.CharField(
                        choices=[
                            ("plain", "plain"),
                            ("http_simple", "http_simple"),
                            ("http_simple_compatible", "http_simple_compatible"),
                            ("http_post", "http_post"),
                            ("tls1.2_ticket_auth", "tls1.2_ticket_auth"),
                        ],
                        default="http_simple",
                        max_length=32,
                        verbose_name="混淆",
                    ),
                ),
                (
                    "obfs_param",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="混淆参数"
                    ),
                ),
                ("level", models.PositiveIntegerField(default=0, verbose_name="用户等级")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ss_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="用户名",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "SS用户",
                "db_table": "user",
                "ordering": ("-last_check_in_time",),
            },
        ),
        migrations.CreateModel(
            name="TrafficLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField(verbose_name="用户id")),
                ("node_id", models.IntegerField(verbose_name="节点id")),
                (
                    "upload_traffic",
                    models.BigIntegerField(
                        db_column="u", default=0, verbose_name="上传流量"
                    ),
                ),
                (
                    "download_traffic",
                    models.BigIntegerField(
                        db_column="d", default=0, verbose_name="下载流量"
                    ),
                ),
                ("rate", models.FloatField(default=1.0, verbose_name="流量比例")),
                ("traffic", models.CharField(max_length=32, verbose_name="流量记录")),
                ("log_time", models.IntegerField(verbose_name="日志时间")),
                (
                    "log_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="记录日期"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "流量记录",
                "db_table": "user_traffic_log",
                "ordering": ("-log_time",),
            },
        ),
    ]
