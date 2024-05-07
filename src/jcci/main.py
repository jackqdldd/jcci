from src.jcci.analyze import JCCI

# 同一分支不同commit比较
commit_analyze = JCCI('https://gitee.com/jackyqidldd/yto-bdtest.git', 'username1')
commit_analyze.analyze_two_commit('master', '6cb574a360c88ff346a9ee26bdf0a2bb8d488f76',
                                  '3d5713cea09b70cfcd8487b685e1b044a577ca9f')

# 分析一个类的方法影响, analyze_class_method方法最后参数为方法所在行数，不同方法行数用逗号分割，不填则分析完整类影响
# class_analyze = JCCI('git@xxxx.git', 'username1')
# class_analyze.analyze_class_method('master','commit_id1', 'package\src\main\java\ClassA.java', '20,81')

# 不同分支比较
# branch_analyze = JCCI('git@xxxx.git', 'username1')
# branch_analyze.analyze_two_branch('branch_new','branch_old')
