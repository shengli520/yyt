# coding=utf-8
import sys

sys.path.append(r"F:\\selenium-py\\")
from framework.base_page import BasePage


class HomePage(BasePage):
    # 行政系统
    xz = "xpath=>.//*[@id='ea-system']/li[3]"

    def click_xz(self):
        self.click(self.xz)

    # *********** 印章管理****************
    # 印章管理
    yzgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/p"
    # 印章刻制申请
    yzkzsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[1]/p"
    # 印章登记查询
    yzdjcx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[2]/p"
    # 印章使用申请
    yzsysq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[3]/p"
    # 借转.报废申请
    jzbfsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[4]/p"
    # 借.转单据查询
    jzdjcx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[5]/p"

    def click_yzgl(self):
        self.click(self.yzgl_btn)

    def click_yzkzsq(self):
        self.click(self.yzkzsq_btn)

    def click_yzdjcx(self):
        self.click(self.yzdjcx_btn)

    def click_yzsysq(self):
        self.click(self.yzsysq_btn)

    def click_jzbfsq(self):
        self.click(self.jzbfsq_btn)

    def click_jzdjcx(self):
        self.click(self.jzdjcx_btn)

    # *********** 空白用印纸管理****************
    # 空白用印纸管理
    kbyyzgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[6]/p"

    # 查询
    cx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[6]/div/p[1]"

    # 保管人申领
    bgrsl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[6]/div/p[2]"

    # 使用人申请
    syrsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[6]/div/p[3]"

    # 核销
    hx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[6]/div/p[4]"

    def click_kbyyzgl(self):
        self.click(self.kbyyzgl_btn)

    def click_cx(self):
        self.click(self.cx_btn)

    def click_bgrsl(self):
        self.click(self.bgrsl_btn)

    def click_syrsq(self):
        self.click(self.syrsq_btn)

    def click_hx(self):
        self.click(self.hx_btn)

    # *********** 证照管理 ****************
    # 证照管理
    zzgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[2]/p"
    # 证照登记查询
    zzdjcx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[2]/div/div[1]/p"
    # 借转.查阅.报废申请
    jzcybfsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[2]/div/div[2]/p"
    # 申请单据查询
    sqdjcx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[2]/div/div[3]/p"
    # 证照下载
    zzxz_btn = "xpath=>.//*[@id='ea-scroll']/div/div[2]/div/div[4]/p"

    def click_zzgl(self):
        self.click(self.zzgl_btn)

    def click_zzdjcx(self):
        self.click(self.zzdjcx_btn)

    def click_jzcybfsq(self):
        self.click(self.jzcybfsq_btn)

    def click_sqdjcx(self):
        self.click(self.sqdjcx_btn)

    def click_zzxz(self):
        self.click(self.zzxz_btn)

    # *********** 项目设立 ****************
    # 项目设立
    xmsl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/p"
    # 项目设立申请
    xmslsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div/p"

    def click_xmsl(self):
        self.click(self.xmsl_btn)

    def click_xmslsq(self):
        self.click(self.xmslsq_btn)

    # *********** 行政服务  ****************
    # 行政服务
    xzfw_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/p"
    # 车辆管理
    clgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[1]/p"
    # 车辆预约
    clyy_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[1]/div/p[1]"
    # 车辆证件管理
    clzjgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[1]/div/p[2]"

    def click_xzfw(self):
        self.click(self.xzfw_btn)

    def click_clgl(self):
        self.click(self.clgl_btn)

    def click_clyy(self):
        self.click(self.clyy_btn)

    def click_clzjgl(self):
        self.click(self.clzjgl_btn)

    # *********** 会所管理  ****************
    # 会所管理
    hsgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[2]/p"
    # 会所信息
    hsxx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[2]/div/p[1]"
    # 会所预订
    hsyd_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[2]/div/p[2]"

    def click_hsgl(self):
        self.click(self.hsgl_btn)

    def click_hsxx(self):
        self.click(self.hsxx_btn)

    def click_hsyd(self):
        self.click(self.hsyd_btn)

    # *********** 会议管理  ****************
    # 会议管理
    hygl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[3]/p"
    # 会议室查询
    hyscx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[3]/div/p[1]"
    # 会议预订
    hyyd_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[3]/div/p[2]"
    # 话费分摊
    hfft_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[3]/div/p[3]"

    def click_hygl(self):
        self.click(self.hygl_btn)

    def click_hyscx(self):
        self.click(self.hyscx_btn)

    def click_hyyd(self):
        self.click(self.hyyd_btn)

    def click_hfft(self):
        self.click(self.hfft_btn)

    # *********** 接待管理  ****************
    # 接待管理
    jdgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[4]/p"
    # 接待申请
    jdsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[4]/div/p[1]"
    # 体验馆申请
    tygsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[4]/div/p[2]"

    def click_jdgl(self):
        self.click(self.jdgl_btn)

    def click_jdsq(self):
        self.click(self.jdsq_btn)

    def click_tygsq(self):
        self.click(self.tygsq_btn)

    # *********** 酒店管理  ****************
    # 酒店管理
    jdgl1_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[5]/p"
    # 客房信息
    kfxx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[5]/div/p[1]"
    # 客房预订
    kfyd_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[5]/div/p[2]"

    def click_jdgl1(self):
        self.click(self.jdgl1_btn)

    def click_kfxx(self):
        self.click(self.kfxx_btn)

    def click_kfyd(self):
        self.click(self.kfyd_btn)

    # *********** 卡位管理  ****************
    # 卡位管理
    kwgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[6]/p"
    # 卡位管理1
    kwgl1_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[6]/div/p[1]"
    # 卡位变更管理
    kwbggl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[6]/div/p[2]"
    # 卡位变更流程
    kwbglc_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[6]/div/p[3]"
    # 卡位费用分摊
    kwfyft_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[6]/div/p[4]"

    def click_kwgl(self):
        self.click(self.kwgl_btn)

    def click_kwgl1(self):
        self.click(self.kwgl1_btn)

    def click_kwbggl(self):
        self.click(self.kwbggl_btn)

    def click_kwbglc(self):
        self.click(self.kwbglc_btn)

    def click_kwfyft(self):
        self.click(self.kwfyft_btn)

    # *********** 快递管理  ****************
    # 快递管理
    kdgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[7]/p"
    # 快递接受
    kjjs_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[7]/div/p[1]"
    # 快件发送
    kjfs_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[7]/div/p[2]"
    # 快递费用统计报表
    kdfytjbb_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[7]/div/p[3]"

    def click_kdgl(self):
        self.click(self.kdgl_btn)

    def click_kjjs(self):
        self.click(self.kjjs_btn)

    def click_kjfs(self):
        self.click(self.kjfs_btn)

    def click_kdfytjbb(self):
        self.click(self.kdfytjbb_btn)

# *********** 名片管理  ****************
    # 名片管理
    mpgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[8]/p"

    # 名片制作申请
    mpzzsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[8]/div/p"

    def click_mpgl(self):
        self.click(self.mpgl_btn)

    def click_mpzzsq(self):
        self.click(self.mpzzsq_btn)

# *********** 单位管理  ****************
    # 单位管理
    dwgl_btn="xpath=>.//*[@id='ea-scroll']/div/div[5]/p"

    #单位信息查询
    dwxxcx_btn="xpath=>.//*[@id='ea-scroll']/div/div[5]/div/div[1]/p"

    #单位业务申请
    dwywsq_btn="xpath=>.//*[@id='ea-scroll']/div/div[5]/div/div[2]/p"

    #业务进度查询
    ywjdcx_btn="xpath=>.//*[@id='ea-scroll']/div/div[5]/div/div[3]/p"

    def click_dwgl(self):
        self.click(self.dwgl_btn)

    def click_dwxxcx(self):
        self.click(self.dwxxcx_btn)

    def click_dwywsq(self):
        self.click(self.dwywsq_btn)

    def click_ywjdcx(self):
        self.click(self.ywjdcx_btn)

# *********** 立政管理  ****************
    #立政管理
    lzgl_btn="xpath=>.//*[@id='ea-scroll']/div/div[8]/p"

    #流程变更查询
    lcbgcx_btn="xpath=>.//*[@id='ea-scroll']/div/div[8]/div/div[1]/p"

    #流程变更管理
    lcbggl_btn="xpath=>.//*[@id='ea-scroll']/div/div[8]/div/div[2]/p"

    #流程新建申请
    lcxjsq_btn="xpath=>.//*[@id='ea-scroll']/div/div[8]/div/div[3]/p"

    def click_lzgl(self):
        self.click(self.lzgl_btn)

    def click_lcbgcx(self):
        self.click(self.lcbgcx_btn)

    def click_lcbggl(self):
        self.click(self.lcbggl_btn)

    def click_lcxjsq(self):
        self.click(self.lcxjsq_btn)

# *********** 资产管理  ****************
    # 资产管理
    zcgl_btn="xpath=>.//*[@id='ea-scroll']/div/div[6]/p"

    #固定资产管理
    gdzcgl_btn="xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[1]/p"

    #资产领用申请
    zclysq_btn="xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[1]/div/p[1]"
    #资产采购查询
    zccgcx_btn="xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[1]/div/p[2]"
    #转移单据查询
    zydjcx_btn="xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[1]/div/p[3]"
    #报废单据查询
    bfdjcx_btn="xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[1]/div/p[4]"
    #资产库查询
    zckcx_btn="xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[1]/div/p[5]"
    #借用单据查询
    jydjcx_btn="xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[1]/div/p[6]"
    #维修单据查询
    wxdjcx_btn="xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[1]/div/p[7]"
    #盘点资产导入
    pdzcdr_btn="xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[1]/div/p[8]"
    #资产撤单申请
    zccdsq_btn="xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[1]/div/p[9]"

    def click_zcgl(self):
        self.click(self.zcgl_btn)

    def click_gdzcgl(self):
        self.click(self.gdzcgl_btn)

    def click_zclysq(self):
        self.click(self.zclysq_btn)

    def click_zccgcx(self):
        self.click(self.zccgcx_btn)

    def click_zydjcx(self):
        self.click(self.zydjcx_btn)

    def click_bfdjcx(self):
        self.click(self.bfdjcx_btn)

    def click_zckcx(self):
        self.click(self.zckcx_btn)

    def click_jydjcx(self):
        self.click(self.jydjcx_btn)

    def click_wxdjcx(self):
        self.click(self.wxdjcx_btn)

    def click_pdzcdr(self):
        self.click(self.pdzcdr_btn)

    def click_zccdsq(self):
        self.click(self.zccdsq_btn)

# *********** 档案管理  ****************
    #档案管理
    dagl_btn="xpath=>.//*[@id='ea-scroll']/div/div[7]/p"
    #业务合同管理
    ywhtgl_btn="xpath=>.//*[@id='ea-scroll']/div/div[7]/div/div[1]/p"
    #业务合同查询
    ywhtcx_btn="xpath=>.//*[@id='ea-scroll']/div/div[7]/div/div[1]/div/p[1]"

    #借用单据查询
    jydjcx_btn2="xpath=>.//*[@id='ea-scroll']/div/div[7]/div/div[1]/div/p[2]"


    def click_dagl(self):
        self.click(self.dagl_btn)

    def click_ywhtgl(self):
        self.click(self.ywhtgl_btn)

    def click_ywhtcx(self):
        self.click(self.ywhtcx_btn)

    def click_jydjcx2(self):
        self.click(self.jydjcx_btn2)

# *********** 行政档案  ****************

    #行政档案
    xzda_btn="xpath=>.//*[@id='ea-scroll']/div/div[7]/div/div[2]/p"
    #业务合同
    ywht_btn="xpath=>.//*[@id='ea-scroll']/div/div[7]/div/div[2]/div/p[1]"
    #品牌授权资质
    ppsqzz_btn="xpath=>.//*[@id='ea-scroll']/div/div[7]/div/div[2]/div/p[2]"


    def click_xzda(self):
        self.click(self.xzda_btn)

    def click_ywht(self):
        self.click(self.ywht_btn)

    def click_ppsqzz(self):
        self.click(self.ppsqzz_btn)

# *********** 档案转移  ****************
    dazy_btn="xpath=>.//*[@id='ea-scroll']/div/div[7]/div/div[3]/p"

    def click_dazy(self):
        self.click(self.dazy_btn)

# *********** 档案借阅  ****************
    dajy_btn = "xpath=>.//*[@id='ea-scroll']/div/div[7]/div/div[4]/p"

    def click_dajy(self):
        self.click(self.dajy_btn)

# *********** 公司发文管理  ****************
    gsfwgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[7]/div/div[5]/p"

    def click_gsfwgl(self):
        self.click(self.gsfwgl_btn)

# *********** 低值易耗品管理  ****************
    #低值易耗品管理
    dzyhpgl_btn="xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[2]/p"
    #采购申请
    cgsq_btn="xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[2]/div/p[1]"
    #领用申请
    lysq_btn="xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[2]/div/p[2]"
    #库存查询
    kccx_btn="xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[2]/div/p[3]"
    #入库单查询
    rkdcx_btn="xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[2]/div/p[4]"
    #库存报表查询
    kcbbcx_btn="xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[2]/div/p[5]"

    def click_dzyhpgl(self):
        self.click(self.dzyhpgl_btn)

    def click_cgsq(self):
        self.click(self.cgsq_btn)

    def click_lysq(self):
        self.click(self.lysq_btn)

    def click_kccx(self):
        self.click(self.kccx_btn)

    def click_rkdcx(self):
        self.click(self.rkdcx_btn)

    def click_kcbbcx(self):
        self.click(self.kcbbcx_btn)

# *********** 无形资产管理  ****************
    #无形资产管理
    wxzcgl_btn="xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[3]/p"

    def click_wxzcgl(self):
        self.click(self.wxzcgl_btn)