# coding=utf-8
import sys

sys.path.append(r"F:\\selenium-py\\")
from framework.base_page import BasePage


class HomePage(BasePage):
    # E-hr系统
    ehr = "xpath=>.//*[@id='ea-system']/li[4]"

    def click_ehr(self):
        self.click(self.ehr)

    # *********** 组织管理****************
    # 组织管理
    zzgl1_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/p"

    def click_zzgl1(self):
        self.click(self.zzgl1_btn)

    # 组织机构查询
    zzjgcx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[1]/p"

    def click_zzjgcx(self):
        self.click(self.zzjgcx_btn)

    # 组织机构调整
    zzjgtz_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[2]/p"

    def click_zzjgtz(self):
        self.click(self.zzjgtz_btn)

    # 组织机构审核人
    zzjgshr_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[3]/p"

    def click_zzjgshr(self):
        self.click(self.zzjgshr_btn)

    # 单位管理
    dwgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[4]/p"

    # 单位审核人查询
    dwshrcx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[5]/p"

    # 绩效单位查询
    jxdwcx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[6]/p"
    # 绩效单位树预算
    jxdwsys_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[7]/p"
    # 绩效单位管理
    jxdwgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[8]/p"
    # 绩效单位申请
    jxdwsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[9]/p"
    # 绩效单位办理
    jxdwbl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[1]/div/div[10]/p"

    def click_dwgl(self):
        self.click(self.dwgl_btn)

    def click_dwshrcx(self):
        self.click(self.dwshrcx_btn)

    def click_jxdwcx(self):
        self.click(self.jxdwcx_btn)

    def click_jxdwsys(self):
        self.click(self.jxdwsys_btn)

    def click_jxdwgl(self):
        self.click(self.jxdwgl_btn)

    def click_jxdwsq(self):
        self.click(self.jxdwsq_btn)

    def click_jxdwbl(self):
        self.click(self.jxdwbl_btn)

    # *********** 招聘管理****************
    # 招聘管理
    zpgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[2]/p"
    # 招聘申请
    zpsq_btn = "css_selector=>.ea-menu-2-title"

    def click_zpgl(self):
        self.click(self.zpgl_btn)

    def click_zpsq(self):
        self.click(self.zpsq_btn)

    # *********** 云计划****************
    # 云计划
    yjh_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/p"

    # 云计划项目申请
    yjhsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[1]/p"

    # 国代资料库
    gdzlk_btn = "xpath=>.//*[@id='ea-scroll']/div/div[3]/div/div[2]/p"

    def click_yjh(self):
        self.click(self.yjh_btn)

    def click_yjhsq(self):
        self.click(self.yjhsq_btn)

    def click_gdzlk(self):
        self.click(self.gdzlk_btn)

    # *********** 培训管理****************

    # 培训管理
    pxgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/p"
    # 讲师管理
    jsgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[1]/p"
    # 课程管理
    kcgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[2]/p"
    # 培训需求
    pxxq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[3]/p"
    # 培训计划
    pxjh_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[4]/p"
    # 培训实施
    pxss_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[5]/p"
    # 培训历史查询
    pxlscx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[6]/p"
    # 试卷管理
    sjgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[7]/p"
    # 360反馈
    fk360_btn = "xpath=>.//*[@id='ea-scroll']/div/div[4]/div/div[8]/p"

    def click_pxgl(self):
        self.click(self.pxgl_btn)

    def click_jsgl(self):
        self.click(self.jsgl_btn)

    def click_kcgl(self):
        self.click(self.kcgl_btn)

    def click_pxxq(self):
        self.click(self.pxxq_btn)

    def click_pxjh(self):
        self.click(self.pxjh_btn)

    def click_pxss(self):
        self.click(self.pxss_btn)

    def click_pxlscx(self):
        self.click(self.pxlscx_btn)

    def click_sjgl(self):
        self.click(self.sjgl_btn)

    def click_360fk(self):
        self.click(self.fk360_btn)

    # *********** 入职管理****************
    # 入职管理
    rzgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[5]/p"
    # 个人资料
    grzl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[5]/div/div[1]/p"
    # 基础信息
    jcxx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[5]/div/div[2]/p"
    # 办公资料
    bgzl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[5]/div/div[3]/p"

    def click_rzgl(self):
        self.click(self.rzgl_btn)

    def click_grzl(self):
        self.click(self.grzl_btn)

    def click_jcxx(self):
        self.click(self.jcxx_btn)

    def click_bgzl(self):
        self.click(self.bgzl_btn)

    # *********** 员工管理****************
    # 员工管理
    yggl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/p"

    # 员工档案
    ygda_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[1]/p"
    # 编外员工
    bwyg_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[2]/p"
    # 员工合同
    yght_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[3]/p"
    # 人事异动
    rsyd_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[4]/p"
    # 实习生解约
    sxsjy_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[5]/p"
    # 离职申请
    lzsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[6]/p"
    # 离职交接
    lzjj_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[7]/p"
    # 追缴流程
    zjlc_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[8]/p"
    # 户口调动
    hkdd_btn = "xpath=>.//*[@id='ea-scroll']/div/div[6]/div/div[9]/p"

    def click_yggl(self):
        self.click(self.yggl_btn)

    def click_ygda(self):
        self.click(self.ygda_btn)

    def click_bwyg(self):
        self.click(self.bwyg_btn)

    def click_yght(self):
        self.click(self.yght_btn)

    def click_rsyd(self):
        self.click(self.rsyd_btn)

    def click_sxsjy(self):
        self.click(self.sxsjy_btn)

    def click_lzsq(self):
        self.click(self.lzsq_btn)

    def click_lzjj(self):
        self.click(self.lzjj_btn)

    def click_zjlc(self):
        self.click(self.zjlc_btn)

    def click_hkdd(self):
        self.click(self.hkdd_btn)

    # *********** 工作计划管理****************
    # 工作计划管理
    gzjhgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[7]/p"

    # 工作报告管理
    gzbggl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[7]/div/div[1]/p"
    # 目标管理
    mbgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[7]/div/div[2]/p"

    def click_gzjhgl(self):
        self.click(self.gzjhgl_btn)

    def click_gzbggl(self):
        self.click(self.gzbggl_btn)

    def click_mbgl(self):
        self.click(self.mbgl_btn)

    # *********** 绩效管理****************
    # 绩效管理
    jxgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[8]/p"
    # 员工绩效管理
    ygjxgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[8]/div/div[1]/p"
    # 员工年度评估
    ygndpg_btn = "xpath=>.//*[@id='ea-scroll']/div/div[8]/div/div[2]/p"
    # 中高层目标责任书
    zgcmbzrs_btn = "xpath=>.//*[@id='ea-scroll']/div/div[8]/div/div[3]/p"
    # 中高层年度评估
    zgcndpg_btn = "xpath=>.//*[@id='ea-scroll']/div/div[8]/div/div[4]/p"
    # 员工等级确认
    ygdjqr_btn = "xpath=>.//*[@id='ea-scroll']/div/div[8]/div/div[5]/p"

    def click_jxgl(self):
        self.click(self.jxgl_btn)

    def click_ygjxgl(self):
        self.click(self.ygjxgl_btn)

    def click_ygndpg(self):
        self.click(self.ygndpg_btn)

    def click_zgcmbzrs(self):
        self.click(self.zgcmbzrs_btn)

    def click_zgcndpg(self):
        self.click(self.zgcndpg_btn)

    def click_ygdjqr(self):
        self.click(self.ygdjqr_btn)

    # *********** 考勤管理****************
    # 考勤管理
    kqgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/p"
    # 请假加班申请
    qjjbsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[1]/p"
    # 考勤明细查询
    kqmxcx_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[2]/p"
    # 员工出差申请
    ygccsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[3]/p"
    # 外出办公申请
    wcbgsq_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[4]/p"
    # 考勤异常管理
    kqycgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[5]/p"
    # 考勤数据报表
    kqsjbb_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[6]/p"
    # 员工考勤确认
    ygkqqr_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[7]/p"
    # 员工调休管理
    ygtxgl_btn = "xpath=>.//*[@id='ea-scroll']/div/div[9]/div/div[8]/p"

    def click_kqgl(self):
        self.click(self.kqgl_btn)

    def click_qjjbsq(self):
        self.click(self.qjjbsq_btn)

    def click_kqmxcx(self):
        self.click(self.kqmxcx_btn)

    def click_ygccsq(self):
        self.click(self.ygccsq_btn)

    def click_wcbgsq(self):
        self.click(self.wcbgsq_btn)

    def click_kqycgl(self):
        self.click(self.kqycgl_btn)

    def click_kqsjbb(self):
        self.click(self.kqsjbb_btn)

    def click_ygkqqr(self):
        self.click(self.ygkqqr_btn)

    def click_ygtxgl(self):
        self.click(self.ygtxgl_btn)
