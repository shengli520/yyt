# coding=utf-8
import sys
sys.path.append(r"F:\\selenium-py\\")
from framework.base_page import BasePage


class HomePage(BasePage):

    #-------**系统页面**-------
    # OA系统
    oa_btn = "xpath=>.//*[@id='ea-system']/li[2]"

    # 行政系统
    xzbg = "partial_link_text=>行政"

    # e-HR系统
    ehr = "partial_link_text=>e-HR"

    # CRM系统
    crm = "partial_link_text=>CRM"

    def click_oa(self):
        self.click(self.oa_btn)

    def click_xzbg(self):
        self.click(self.xzbg)

    def click_ehr(self):
        self.click(self.ehr)

    def click_crm(self):
        self.click(self.crm)


# *********** 对外投资****************
    # 对外投资
    dwtz_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/p"

    # 控股
    kg_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[1]/p"

    # 参股
    cg_btm = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[2]/p"

    # 其他
    qt_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[3]/p"

    # 断言字段
    ywmsxz_txt = "id=>businessmodel"

    def get_ywmsxz(self):
        return self.get_txt(self.ywmsxz_txt)

    def click_dwtz(self):
        self.click(self.dwtz_btn)

    def click_kg(self):
        self.click(self.kg_btn)

    def click_cg(self):
        self.click(self.cg_btm)

    def click_qt(self):
        self.click(self.qt_btn)


# *********** 员工通讯录****************
    # EA通讯录
    eatxl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[2]/p"

    # 员工通讯录
    ygtxl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[2]/div/div/p"

    # 你是谁？
    who_btn = "xpath=>.//*[@id='conditions_table']/tbody/tr[1]/td[1]/a"

    # 员工工号
    code_btn = "id=>employeecode"

    def click_eatxl(self):
        self.click(self.eatxl_btn)

    def click_ygtxl(self):
        self.click(self.ygtxl_btn)
        self.sleep(0.2)

    def click_who(self):
        self.click(self.who_btn)

    def get_text(self):
        t = self.get_txt(self.code_btn)
        return t

# *********** 财务管理模块****************
    # 财务管理
    cwgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/p"

    def click_cwgl(self):
        self.click(self.cwgl_btn)

    # 费用报销
    fybx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[1]/p"

    # 断言字段 单据编号
    djbh = "xpath=>html/body/table/tbody/tr[6]/td/table/tbody/tr/td[2]"

    def click_fybx(self):
        self.click(self.fybx_btn)

    def get_djbh(self):
        t = self.get_txt(self.djbh)
        return t

   # ***********************借款申请*******************
    # 借款申请
    jksq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[2]/p"

    # 断言字段 单据编号
    jk_djbh = "xpath=>html/body/table/tbody/tr[5]/td/table/tbody/tr/td[2]"

    def click_jksq(self):
        self.click(self.jksq_btn)

    def get_jkdjbh(self):
        return self.get_txt(self.jk_djbh)

    # ***********************预算查询*******************
    # 预算查询
    yscx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[3]/p"

    # 断言字段 预算部门
    ys_yubm = "xpath=>.//*[@id='results_table']/tbody/tr/td[2]"

    def click_yscx(self):
        self.click(self.yscx_btn)

    def get_ysyubm(self):
        return self.get_txt(self.ys_yubm)

    #***********************还款申请*******************

    # 还款申请
    hksq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[4]/p"

    # 断言字段 还款类型

    hk_hklx = "xpath=>html/body/table/tbody/tr[5]/td/table/tbody/tr/td[3]"

    def click_hksq(self):
        self.click(self.hksq_btn)

    def get_hklx(self):
        return self.get_txt(self.hk_hklx)

    # ***********************应收异常申请*******************

    # 应收异常申请
    ysycsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[5]/p"

    # 断言字段 结算客户
    ys_jskh = "id=>customername"

    def click_ysycsq(self):
        self.click(self.ysycsq_btn)

    def get_jskh(self):
        return self.get_txt(self.ys_jskh)

    # ***********************异常费用申请*******************

    # 异常费用申请
    ycfysq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[6]/p"

    # 断言字段 费用支付单位

    fyzfdw_txt = "id=>payunit"

    def click_ycfysq(self):
        self.click(self.ycfysq_btn)

    def get_fyzfdw(self):
        return self.get_txt(self.fyzfdw_txt)

    # ***********************借款统计*******************

    # 借款统计
    jktj_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[7]/p"

    # 断言字段 借款人姓名
    jkrxm_txt = "xpath=>html/body/table/tbody/tr[5]/td/table/tbody/tr/td[2]"

    def click_jktj(self):
        self.click(self.jktj_btn)

    def get_jkrxm(self):
        return self.get_txt(self.jkrxm_txt)

    # ***********************预算管理*******************

    # 预算管理
    ysgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[8]/p"

    # 预算申请
    yssq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[8]/div/p[1]"

    # 断言字段 预算部门
    ysbm_txt = "xpath=>html/body/table/tbody/tr[3]/td/table/tbody/tr/td[5]"

    def click_ysgl(self):
        self.click(self.ysgl_btn)

    def click_yssq(self):
        self.click(self.yssq_btn)

    def get_ysbm(self):
        return self.get_txt(self.ysbm_txt)

    # 预算调整
    ystz_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[8]/div/p[2]"

    # 断言字段 预算年度
    ysnd_txt = "xpath=>html/body/table/tbody/tr[3]/td/table/tbody/tr/td[3]"

    def click_ystz(self):
        self.click(self.ystz_btn)

    def get_ysnd(self):
        return self.get_txt(self.ysnd_txt)

    # 额度管理
    edgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[8]/div/p[3]"

    # 断言字段 额度类型
    edlx_txt = "xpath=>.//*[@id='results_table']/tbody/tr/td[6]"

    def click_edgl(self):
        self.click(self.edgl_btn)

    def get_edlx(self):
        return self.get_txt(self.edlx_txt)

    # 额度比例申请
    edblsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[8]/div/p[4]"

    # 断言字段 billcode
    billcode_txt = "id=>billcode"

    def click_edblsq(self):
        self.click(self.edblsq_btn)

    def get_billcode(self):
        return self.get_txt(self.billcode_txt)

    # 额度报表
    edbb_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[8]/div/p[5]"

    # 断言字段 年度
    nd_txt = "xpath=>.//*[@id='results_table']/tbody/tr/td[3]"

    def click_edbb(self):
        self.click(self.edbb_btn)

    def get_nd(self):
        return self.get_txt(self.nd_txt)

     # ***********************押金项目*******************

     # 押金项目
     #
    yjxm_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[9]/p"

    # 押金记录

    yjjl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[9]/div/p[1]"

    # 断言字段 押金金额
    yjje_txt = "id=>depositamount"

    def click_yjxm(self):
        self.click(self.yjxm_btn)

    def click_yjjl(self):
        self.click(self.yjjl_btn)

    def get_yjje(self):
        return self.get_txt(self.yjje_txt)

    # 押金流程
    yjlc_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[9]/div/p[2]"

    # 断言字段 币种
    bz_txt = "id=>currency"

    def click_yjlc(self):
        self.click(self.yjlc_btn)

    def get_bz(self):
        return self.get_txt(self.bz_txt)

    # ***********************虚拟经营单位管理*******************

    # 虚拟经营单位管理

    xnjydwgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[10]/p"

    # 断言字段 公司编码
    gsbm_txt = "id=>unitcode"

    def click_xnjydwgl(self):
        self.click(self.xnjydwgl_btn)

    def get_gsbm(self):
        return self.get_txt(self.gsbm_txt)

    # ***********************其他费用支付*******************
    #
    # 其他费用支付
    qtfyzf_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[11]/p"

    # 断言字段 支付单位
    zfdw_txt = "xpath=>html/body/table[4]/tbody/tr/td[5]"

    def click_qtfyzf(self):
        self.click(self.qtfyzf_btn)

    def get_zfdw(self):
        return self.get_txt(self.zfdw_txt)

    # ***********************核算初始化*******************
    #
    # 核算初始化
    hscsh_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[12]/p"

    def click_hscsh(self):
        self.click(self.hscsh_btn)

    # ***********************NC反结账申请*******************
    # NC反结账申请
    fjzsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[13]/p"

    # 断言字段 单据状态
    ztbm_txt = "id=>ordermoney"

    def click_fjzsq(self):
        self.click(self.fjzsq_btn)

    def get_ztbm(self):
        return self.get_txt(self.ztbm_txt)

    # ***********************会计报表管理档案*******************
    # 会计报表管理档案
    kjda_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[15]/p"

    # 断言字段 年月
    ny_txt = "xpath=>html/body/table[3]/tbody/tr/td[5]"

    def click_kjad(self):
        self.click(self.kjda_btn)

    def get_ny(self):
        return self.get_txt(self.ny_txt)

    # ***********************撤消单据审批*******************

    # 撤消单据审批
    cxdjsp_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[16]/p"

    # 断言字段 撤销单据类型
    cxdjlx_txt = "xpath=>html/body/div[2]/table/tbody/tr/td[3]"

    def click_cxdjsp(self):
        self.click(self.cxdjsp_btn)

    def get_cxdjlx(self):
        return self.get_txt(self.cxdjlx_txt)

# 3 **************************************************************--------
# ************************************************************************************************************************************************************
#***************************************************----- 税务管理 ---- ******

    # 税务管理
    swgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/p"

    # 基本信息
    jbxx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[1]/p"

    # 断言字段 单位编码
    dwbm_txt = "id=>unitcode"

    def click_swgl(self):
        self.click(self.swgl_btn)

    def click_jbxx(self):
        self.click(self.jbxx_btn)

    def get_dwbm(self):
        return self.get_txt(self.dwbm_txt)

    # ***********************税务减免*******************
    # 税务减免
    swjm_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[2]/p"

    # 断言字段，税种
    sz_txt = "xpath=>html/body/table[3]/tbody/tr/td[5]"

    def click_swjm(self):
        self.click(self.swjm_btn)

    def get_sz(self):
        return self.get_txt(self.sz_txt)

    # ***********************税务处罚*******************
    # 税务处罚
    swcf_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[3]/p"

    # 断言字段，处罚币种
    cfbz_txt = "xpath=>html/body/table[3]/tbody/tr/td[7]"

    def click_swcf(self):
        self.click(self.swcf_btn)

    def get_cfbz(self):
        return self.get_txt(self.cfbz_txt)

    # ***********************增值税申报*******************
    # 增值税申报
    zzssb_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[4]/p"

    # 断言字段，税种类型
    szlx_txt = "xpath=>html/body/table[3]/tbody/tr/td[5]"

    def click_zzssb(self):
        self.click(self.zzssb_btn)

    def get_szlx(self):
        return self.get_txt(self.szlx_txt)

    # ***********************营业税申报*******************
    # 营业税申报
    yyssb_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[5]/p"

    # 断言字段，  缴纳确认单据
    jnqrdj_txt = "xpath=>html/body/table[3]/tbody/tr/td[3]"

    def click_yyssb(self):
        self.click(self.yyssb_btn)

    def get_jnqrdj(self):
        return self.get_txt(self.jnqrdj_txt)

    # ***********************附加税申报*******************
    # 附加税申报
    fjssb_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[6]/p"

    # 断言字段，  录入人
    llr_txt = "xpath=>html/body/table[3]/tbody/tr/td[6]"

    def click_fjssb(self):
        self.click(self.fjssb_btn)

    def get_lrr(self):
        return self.get_txt(self.llr_txt)

    # ***********************其他税种申报*******************
    # 其他税种申报
    qtszsb_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[7]/p"

    # 断言字段，  录入时间
    lrsj_txt = "xpath=>html/body/table[3]/tbody/tr[1]/td[7]"

    def click_qtszsb(self):
        self.click(self.qtszsb_btn)

    def get_lrsj(self):
        return self.get_txt(self.lrsj_txt)

    # ***********************所得税申报*******************
    # 所得税申报
    sdssb_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[8]/p"

    # 断言字段，  税款所属时间
    sksssj_txt = "xpath=>html/body/table[3]/tbody/tr/td[6]"

    def click_sdssb(self):
        self.click(self.sdssb_btn)

    def get_sksssj(self):
        return self.get_txt(self.sksssj_txt)

    # ***********************未申报查询*******************
    # 未申报查询
    wsbcx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[9]/p"

    # 断言字段，  所属平台
    sspt_txt = "xpath=>html/body/div[3]/table[2]/tbody/tr/td[5]"

    def click_wsbcx(self):
        self.click(self.wsbcx_btn)

    def get_sspt(self):
        return self.get_txt(self.sspt_txt)

    # ***********************税收分类库*******************
    # 税收分类库
    ssflk_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[10]/p"

    # 断言字段，  合并编码
    hbbm_txt = "xpath=>.//*[@id='condition']/div[2]/div/div/div/div[2]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/span[1]"

    def click_ssflk(self):
        self.click(self.ssflk_btn)

    def get_hbbm(self):
        return self.get_txt(self.hbbm_txt)

# 3 **************************************************************--------
# ************************************************************************************************************************************************************
#***************************************************----- 法务管理 ---- ******

    # 法务管理
    fwgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[5]/p"

    # 超期项目管理
    cqxmgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[5]/div/div[1]/p"

    # 超期项目申请
    cqxmsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[5]/div/div[1]/div/p[1]"

    # 律师函申请
    lshsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[5]/div/div[1]/div/p[2]"

    # 诉讼程序申请
    sscxsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[5]/div/div[1]/div/p[3]"

    # 律师函统计
    lshtj_btn = "xpath=>.//*[@id='ea-scroll']/div/div[5]/div/div[1]/div/p[4]"

    def click_fwgl(self):
        self.click(self.fwgl_btn)

    def click_cqxmgl(self):
        self.click(self.cqxmgl_btn)

    def click_cqxmsq(self):
        self.click(self.cqxmsq_btn)

    def click_lshsq(self):
        self.click(self.lshsq_btn)

    def click_sscxsq(self):
        self.click(self.sscxsq_btn)

    def click_lshtj(self):
        self.click(self.lshtj_btn)


# ***********************诉讼案件归档管理*******************
    # 诉讼案件归档管理
    ssgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[5]/div/div[2]/p"
    # 案件基础信息表
    ajjcxxb_btn = "xpath=>.//*[@id='ea-scroll']/div/div[5]/div/div[2]/div/p[1]"
    # 案件程序信息表
    ajcxxxb_btn = "xpath=>.//*[@id='ea-scroll']/div/div[5]/div/div[2]/div/p[2]"

    # 案件进度汇报表
    ajjdhbb_btn = "xpath=>.//*[@id='ea-scroll']/div/div[5]/div/div[2]/div/p[3]"

    # 报表统计
    bbtj_btn = "xpath=>.//*[@id='ea-scroll']/div/div[5]/div/div[2]/div/p[4]"

    def click_ssgl(self):
        self.click(self.ssgl_btn)

    def click_ajjcxxb(self):
        self.click(self.ajjcxxb_btn)

    def click_ajcxxxb(self):
        self.click(self.ajcxxxb_btn)

    def click_ajjdhbb(self):
        self.click(self.ajjdhbb_btn)

    def click_bbtj(self):
        self.click(self.bbtj_btn)


# 3 **************************************************************--------
# ************************************************************************************************************************************************************
#***************************************************----- 营运管理 ---- ******

    # 营运管理
    yygl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/p"

    # 批文管理
    pwgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[1]/p"

    # 报告委托书申请
    bgwtssq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[1]/div/p[2]"
    # 报告委托书查询
    bgwtscx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[1]/div/p[1]"

    # 断言 状态
    zt_txt = "xpath=>html/body/table/tbody/tr[6]/td/table/tbody/tr/td[3]"

    # 断言 经营单位
    jydw_txt = "xpath=>html/body/table/tbody/tr[6]/td/table/tbody/tr/td[3]"

    def get_zt(self):
        return self.get_txt(self.zt_txt)

    def get_jydw(self):
        return self.get_txt(self.jydw_txt)

    def click_yygl(self):
        self.click(self.yygl_btn)

    def click_pwgl(self):
        self.click(self.pwgl_btn)

    def click_bgwtssq(self):
        self.click(self.bgwtssq_btn)

    def click_bgwtscx(self):
        self.click(self.bgwtscx_btn)

# ***********************异常管理*******************
    # 异常管理
    ycgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[2]/p"

    # 运作异常
    yzyc_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[2]/div/p[1]"

    # 异常赔偿费用
    ycpcfy_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[2]/div/p[2]"

    # 应收款库存异常
    yskkcyc_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[2]/div/p[3]"
    # 货权转移查询
    hqzycx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[2]/div/p[4]"

    # 单据编号 断言
    cybh_txt = "id=>billsn"

    cydjbh_txt = "id=>billcode"

    def get_cydjbh(self):
        return self.get_txt(self.cydjbh_txt)

    def get_cybh(self):
        return self.get_txt(self.cybh_txt)

    def click_ycgl(self):
        self.click(self.ycgl_btn)

    def click_yzyc(self):
        self.click(self.yzyc_btn)

    def click_ycpcfy(self):
        self.click(self.ycpcfy_btn)

    def click_yskkcyc(self):
        self.click(self.yskkcyc_btn)

    def click_hqzycx(self):
        self.click(self.hqzycx_btn)


# ***********************库存管理*******************
   # 库存管理
    kcgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[3]/p"

   # 仓库管理
    ckgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[3]/div/p[1]"

   # 仓库使用率
    cksyl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[3]/div/p[2]"

   # 运输车辆
    yscl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[3]/div/p[3]"

   # 物流资源汇总
    wlzyhz_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[3]/div/p[4]"

   # 车辆信息统计表
    clxxtjb_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[3]/div/p[5]"

    def click_kcgl(self):
        self.click(self.kcgl_btn)

    def click_ckgl(self):
        self.click(self.ckgl_btn)

    def click_cksyl(self):
        self.click(self.cksyl_btn)

    def click_yscl(self):
        self.click(self.yscl_btn)

    def click_wlzyhz(self):
        self.click(self.wlzyhz_btn)

    def click_clxxtjb(self):
        self.click(self.clxxtjb_btn)

# ***********************核销单管理*******************
    # 核销单管理
    hxdgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[4]/p"

    # 核销单查询
    hxdcx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[4]/div/p[1]"

    # 核销单申请
    hxdsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[4]/div/p[2]"

    def click_hxdgl(self):
        self.click(self.hxdgl_btn)

    def click_hxdcx(self):
        self.click(self.hxdcx_btn)

    def click_hxdsq(self):
        self.click(self.hxdsq_btn)


# ***********************项目分摊管理*******************
    # 项目分摊管理
    xmftgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[5]/p"

    # 业务部门导入
    ywbmdr_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[5]/div/p[1]"

    # 项目清单导入
    xmqddr_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[5]/div/p[2]"

    # 项目分摊人员
    xmftry_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[5]/div/p[3]"

    # 人员项目占比
    ryxmzb_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[5]/div/p[4]"

    def click_xmftgl(self):
        self.click(self.xmftgl_btn)

    def click_ywbmdr(self):
        self.click(self.ywbmdr_btn)

    def click_xmqddr(self):
        self.click(self.xmqddr_btn)

    def click_xmftry(self):
        self.click(self.xmftry_btn)

    def click_ryxmzb(self):
        self.click(self.ryxmzb_btn)

# ***********************工作任务分派督办*******************
    # 工作任务分派督办
    gzrwfpdb_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[6]/p"

    gzrwfpdb1_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[6]/div/p"

    def click_gzrw(self):
        self.click(self.gzrwfpdb_btn)

    def click_gzrw1(self):
        self.click(self.gzrwfpdb1_btn)

# ***********************方案审批*******************
    # 方案审批
    fasp_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[7]/p"

    def click_fasp(self):
        self.click(self.fasp_btn)


# ***********************400电话管理 *******************
    # 400电话管理
    dhgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[8]/p"

    def click_dhgl(self):
        self.click(self.dhgl_btn)

# 3 **************************************************************--------
# ************************************************************************************************************************************************************
#***************************************************----- 审计管理 ---- ******
    # 审计管理
    sjgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[7]/p"

    # 审计简报
    sjjb_btn = "xpath=>.//*[@id='ea-scroll']/div/div[7]/div/div[1]/p"

    # 审计计划
    sjjh_btn = "xpath=>.//*[@id='ea-scroll']/div/div[7]/div/div[2]/p"

    def click_sjgl(self):
        self.click(self.sjgl_btn)

    def click_sjjb(self):
        self.click(self.sjjb_btn)

    def click_sjjh(self):
        self.click(self.sjjh_btn)
# 3 **************************************************************--------
# ************************************************************************************************************************************************************
#***************************************************----- 证券管理 ---- ******

    # 证券管理
    zqgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[8]/p"

    # 投资管理
    tzgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[8]/div/div[1]/p"

    def click_zqgl(self):
        self.click(self.zqgl_btn)

    def click_tzgl(self):
        self.click(self.tzgl_btn)

# ***********************重要信息批露 *******************

    # 重要信息批露
    zyxx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[8]/div/div[2]/p"
    # 重要信息批露2
    zyxx2_btn = "xpath=>.//*[@id='ea-scroll']/div/div[8]/div/div[2]/div/p[1]"
    # 担保数据维护
    dbsjwh_btn = "xpath=>.//*[@id='ea-scroll']/div/div[8]/div/div[2]/div/p[2]"
    # 两会过会公司
    lhghgs_btn = "xpath=>.//*[@id='ea-scroll']/div/div[8]/div/div[2]/div/p[3]"
    # 资金担保申请
    zjdbsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[8]/div/div[2]/div/p[4]"

    def click_zyxx(self):
        self.click(self.zyxx_btn)

    def click_zyxx2(self):
        self.click(self.zyxx2_btn)

    def click_dbsjwh(self):
        self.click(self.dbsjwh_btn)

    def click_lhghgs(self):
        self.click(self.lhghgs_btn)

    def click_zjdbsq(self):
        self.click(self.zjdbsq_btn)

# 3 **************************************************************--------
# ************************************************************************************************************************************************************
#***************************************************----- IT服务 ---- ******
    # IT服务
    itfw_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/p"
    # 系统需求申请
    xtxqsq_btn = "x=>.//*[@id='ea-scroll']/div/div[9]/div/div[1]/p"
    # 系统需求申请2
    xtxqsq2_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[1]/div/p"

    def click_itfw(self):
        self.click(self.itfw_btn)

    def click_xtxqsq(self):
        self.click(self.xtxqsq_btn)

    def click_xtxqsq2(self):
        self.click(self.xtxqsq2_btn)

# ***********************BUGLIST *******************
    # BUG-LIST
    buglist_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[2]/p"

    # bug
    bug_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[2]/div/p[1]"

    # 版本
    bb_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[2]/div/p[2]"

    def click_buglist(self):
        self.click(self.buglist_btn)

    def click_bug(self):
        self.click(self.bug_btn)

    def click_bb(self):
        self.click(self.bb_btn)


# ***********************用户评价 *******************
    # 用户评价
    yhpj_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[3]/p"

    def click_yhpj(self):
        self.click(self.yhpj_btn)

# ***********************IT服务申请 *******************
    # IT服务申请
    itfwsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[4]/p"

    # 软件登记管理
    rjdjgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[4]/div/p[1]"
    # 虚拟机申请
    xnjsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[4]/div/p[2]"
    # 系统停机申请
    xttjsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[4]/div/p[3]"
    # 系统停机日志
    xttjrz_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[4]/div/p[4]"

    def click_itfwsq(self):
        self.click(self.itfwsq_btn)

    def click_rjdjgl(self):
        self.click(self.rjdjgl_btn)

    def click_xnjsq(self):
        self.click(self.xnjsq_btn)

    def click_xttjsq(self):
        self.click(self.xttjsq_btn)

    def click_xttjrz(self):
        self.click(self.xttjrz_btn)

# ***********************权限管理 *******************
    # 权限管理
    qxgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[5]/p"

    # 工作流授权
    gzlsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[5]/div/p[1]"

    # 系统授权申请

    xtsqsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[5]/div/p[2]"

    def click_qxgl(self):
        self.click(self.qxgl_btn)

    def click_gzlsq(self):
        self.click(self.gzlsq_btn)

    def click_xtsqsq(self):
        self.click(self.xtsqsq_btn)


# ***********************开户申请(非OA) *******************
    # 开户申请(非OA)
    khsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[6]/p"

    def click_khsq(self):
        self.click(self.khsq_btn)


# ***********************邮箱管理 *******************
    # 邮箱管理
    yxgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[7]/p"

    # 特殊邮箱申请
    tsyxsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[7]/div/p[1]"
    # 临时邮件组管理
    lsyjzgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[7]/div/p[2]"
    # 邮件组发送申请
    yjzfssq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[7]/div/p[3]"

    def click_yxgl(self):
        self.click(self.yxgl_btn)

    def click_tsyxsq(self):
        self.click(self.tsyxsq_btn)

    def click_lsyjzgl(self):
        self.click(self.lsyjzgl_btn)

    def click_yjzfssq(self):
        self.click(self.yjzfssq_btn)


# ***********************知识库管理*******************
    # 知识库管理
    zskgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[8]/p"

    def click_zskgl(self):
        self.click(self.zskgl_btn)


# ***********************个人工作台*******************
    # 个人工作台
    grgzt_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[9]/p"

    # oa审核页面
    oashym_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[9]/div/p"

    def click_grgzt(self):
        self.click(self.grgzt_btn)

    def click_oashym(self):
        self.click(self.oashym_btn)

# 3 **************************************************************--------
# ************************************************************************************************************************************************************
#***************************************************----- 系统维护 ---- ******
    # 系统维护
    xtwh_btn = "xpath=>.//*[@id='ea-scroll']/div/div[10]/p"

    # 系统管理
    xtgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[10]/div/div[1]/p"
    #######系统授权申请  重复菜单#########

    # 系统日志查询
    xtrzxc_btn = "xpath=>.//*[@id='ea-scroll']/div/div[10]/div/div[1]/div/p[2]"
    # 单据审核
    djsh_btn = "xpath=>.//*[@id='ea-scroll']/div/div[10]/div/div[1]/div/p[3]"

    # 帮助文档
    bzwd_btn = "xpath=>.//*[@id='ea-scroll']/div/div[10]/div/div[1]/div/p[4]"

    # MQ日志查询
    mqrzcx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[10]/div/div[1]/div/p[5]"

    # 系统执行时长报表
    xtzxscbb_btn = "xpath=>.//*[@id='ea-scroll']/div/div[10]/div/div[1]/div/p[6]"

    def click_xtwh(self):
        self.click(self.xtwh_btn)

    def click_xtgl(self):
        self.click(self.xtgl_btn)

    def click_xtrzxc(self):
        self.click(self.xtrzxc_btn)

    def click_djsh(self):
        self.click(self.djsh_btn)

    def click_bzwd(self):
        self.click(self.bzwd_btn)

    def click_mqrzcx(self):
        self.click(self.mqrzcx_btn)

    def click_xtzxscbb(self):
        self.click(self.xtzxscbb_btn)

# ***********************工作流管理*******************

    # 工作流管理
    gzlgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[10]/div/div[2]/p"

    # 设置流程类别管理员
    # xtgl_btn="xpath=>.//*[@id='ea-scroll']/div/div[10]/div/div[2]/div/p[1]"

    # 流程审核人预览
    lcshryl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[10]/div/div[2]/div/p[2]"
    # 流程审核人查询
    lcshrcx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[10]/div/div[2]/div/p[3]"

    # 流程变更审批
    lcbgsp_btn = "xpath=>.//*[@id='ea-scroll']/div/div[10]/div/div[2]/div/p[4]"

    # 设置流程类别管理员
    szlclb_btn = "xpath=>.//*[@id='ea-scroll']/div/div[10]/div/div[2]/div/p[5]"

    # 操作指引
    czzy_btn = "xpath=>.//*[@id='ea-scroll']/div/div[10]/div/div[2]/div/p[6]"

    def click_gzlgl(self):
        self.click(self.gzlgl_btn)

    def click_lcshryl(self):
        self.click(self.lcshryl_btn)

    def click_lcshrcx(self):
        self.click(self.lcshrcx_btn)

    def click_lcbgsp(self):
        self.click(self.lcbgsp_btn)

    def click_szlclb(self):
        self.click(self.szlclb_btn)

    def click_czzy(self):
        self.click(self.czzy_btn)

    # def click_xtzxscbb(self):
    #     self.click(self.xtzxscbb_btn)
