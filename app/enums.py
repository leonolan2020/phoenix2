from django.db.models import TextChoices
from django.utils.translation import gettext as _
from enum import Enum
from dashboard import enums as DashboardEnum

class ParametersEnum(TextChoices):
    GOOGLE_GPS_X='GOOGLE_GPS_X',_('GOOGLE_GPS_X')
    GOOGLE_GPS_Y='GOOGLE_GPS_Y',_('GOOGLE_GPS_Y')
    GOOGLE_API_KEY='GOOGLE_API_KEY',_('GOOGLE_API_KEY')
    ABOUT_US='درباره ما کامل',_('درباره ما کامل')
    ABOUT_US_SHORT='درباره ما کوتاه',_('درباره ما کوتاه')
    ABOUT_US_TITLE='عنوان درباره ما',_('عنوان درباره ما')
    ADDRESS='آدرس',_('آدرس')
    CURRENCY='واحد پول',_('واحد پول')
    CONTACT_US='ارتباط با ما',_('ارتباط با ما')
    CSRF_FAILURE_MESSAGE='پیام درخواست نامعتبر',_('پیام درخواست نامعتبر')
    EMAIL='ایمیل',_('ایمیل')
    FAX='فکس',_('فکس')
    GOOGLE_SEARCH_CONSOLE_TAG='تگ سرچ گوگل',_('تگ سرچ گوگل')
    LOCATION='موقعیت در گوگل مپ',_('موقعیت در گوگل مپ')     
    MOBILE='موبایل',_('موبایل')
    NAV_BACK_COLOR='رنگ زمینه منوی بالای سایت',_('رنگ زمینه منوی بالای سایت')
    NAV_TEXT_COLOR='رنگ متن منوی بالای سایت',_('رنگ متن منوی بالای سایت')
    OUR_TEAM_LINK='لینک تیم ما',_('لینک تیم ما')
    OUR_TEAM_TITLE='عنوان تیم ما',_('عنوان تیم ما')
    POSTAL_CODE='کد پستی',_('کد پستی')
    PRE_TILTE='پیش عنوان',_('پیش عنوان')
    SLOGAN='شرح کوتاه',_('شرح کوتاه')
    TEL='تلفن',_('تلفن')
    TERMS='قوانین',_('قوانین')
    THEME_COLOR='رنگ سربرگ کروم در موبایل',_('رنگ سربرگ کروم در موبایل')
    TITLE='عنوان',_('عنوان')
    URL='لینک',_('لینک')
    VIDEO_LINK='لینک ویدیو',_('لینک ویدیو')
    VIDEO_TITLE='عنوان ویدیو',_('عنوان ویدیو')
    





class MainPicEnum(TextChoices):    
    FAVICON='آیکون سایت',_('آیکون سایت')     
    CAROUSEL='سایت',_('سایت')    
    FAQ='سوالات',_('سوالات')     
    SEARCH='جستجو',_('جستجو')    
    VIDEO='ویدیو',_('ویدیو')
    ABOUT='درباره ما',_('درباره ما')
    CONTACT_HEADER='سربرگ ارتباط با ما',_('سربرگ ارتباط با ما')
    LOADING='لودینگ',_('لودینگ')
    LOGO='لوگو',_('لوگو')
    BIG_LOGO='لوگوی بزرگ',_('لوگوی بزرگ')
    DARK_LOGO='لوگوی تیره',_('لوگوی تیره')
    LIGHT_LOGO='لوگوی روشن',_('لوگوی روشن')
    BLOG_HEADER='سربرگ مقاله',_('سربرگ مقاله')
    OUR_WORK_HEADER='سربرگ پروژه',_('سربرگ پروژه')
    PAGE_HEADER_DEFAULT='سربرگ پیش فرض برای صفحات',_('سربرگ پیش فرض برای صفحات')
    ABOUT_HEADER='سربرگ درباره ما',_('سربرگ درباره ما')
    TAG_HEADER='سربرگ برچسب',_('سربرگ برچسب')
   