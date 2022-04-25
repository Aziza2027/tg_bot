from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from loader import dp, bot

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)

@dp.message_handler(text_contains=("Abu Bakr As-Siddiq r.a"))
async def send_photo01(message: types.Message):
    photo_file = InputFile(path_or_bytesio="photos/sahoba01.jpg")
    await message.reply_photo(photo_file, caption="Abu Bakr As-Siddiq (573-634)Abu Bakrga 'As-Siddiq' (Haqiqatni tasdiqlovchi) unvoni berildi. \n "
                                                  "U Muhammad (Sollollohu Alayhi Vasallam)dan ikki yarim yosh kichik va erkaklar orasida birinchi bo'lib Islomga kirgan inson edi. \n"
                                                  "U har doim Muhammad (Sollollohu Alayhi Vasallam.)ning juda yaqin hamrohi bo'lgan. Va u Rasulullohni boshqa odamlardan ko'ra yaxshiroq bilar edi.")

@dp.message_handler(text_contains=("Umar ibn Xattob r.a"))
async def send_photo02(message: types.Message):
    photo_file = InputFile(path_or_bytesio="photos/sahoba02.jpg")
    await message.reply_photo(photo_file, caption="Umar ibn Xattob (584-644)U Banu Adi qabilasidan bo'lgan. Umar ibn Xattob (r.a.) tarixda tanilgan eng qudratli va eng nufuzli xalifalardan biri bo'lgan.\n"
                                                  " U Abu Bakrdan keyingi ikkinchi xalifa bo'lgan. Bu odamning ismi adolat va haqiqat, kuch va jasorat, zohidlik va xudojo'ylik bilan birlashtirilgan.U juda taqvodor edi. \n"
                                                  "U Allohdan qo'rqar, va unga Alloh eslatilsa, yig'lab yuborar edi. U Rasululloh (s.a.v.)ning qayniotalaridan bir bo'lgan. \n"
                                                  "Uning Islomni qabul qilishi da'vatning yangi bosqichini boshlab bergan.")

@dp.message_handler(text_contains=("Usmon ibn Affon r.a"))
async def send_photo03(message: types.Message):
    photo_file = InputFile(path_or_bytesio="photos/sahoba03.jpg")
    await message.reply_photo(photo_file, caption="Usmon ibn Affon (577-656)Usmon ibn Affon (r.a.) Fil yilidan taxminan olti yil o'tgacha,\n "
                                                  "Makka yaqinidagi Toif shahrida Qurayshning boy oilasida tug'ilgan. \n"
                                                  "U butun hayoti davomida mehribon, saxiy odam edi va Islomni qabul qilguniga qadar ham muhtojlarga yordam uchun pul berib turardi.\n"
                                                  "Usmonning Payg'ambar ﷺning ikki qiziga uylanishi unga 'Zun-Nurayn' (ikki nur egasi) taxallusini bergan.")

@dp.message_handler(text_contains=("Ali ibn Abu Tolib r.a"))
async def send_photo04(message: types.Message):
    photo_file = InputFile(path_or_bytesio="photos/sahoba04.jpg")
    await message.reply_photo(photo_file, caption="Ali ibn Abu Tolib (600-661)Ali ibn Abu Tolib (r.a.) Fil yilining 13-Rajab oyida tug'ilgan.\n"
                                                  " Ali va payg'ambar ﷺ o'rtasidagi sevgi ilohiy edi. Chunki ularning umumiy jihatlari ko'p edi.\n"
                                                  " U Rasululloh ﷺning barcha yurishlarida ishtirok etgan. \n"
                                                  "Ali qo'rqmas va sodiq jangchi, o'ta taqvodor inson va mohir notiq edi.Ali ibn Abu Tolib (r.a.) mo'minlarning onasi, \n"
                                                  "Rasululloh ﷺning suyukli qizlari Fotimai Zahroga uylangan.")

@dp.message_handler(text_contains=("Abdurahmon ibn avf"))
async def send_photo01(message: types.Message):
    photo_file = InputFile(path_or_bytesio="photos/sahoba04.jpg")
    await message.reply_photo(photo_file, caption="Abdurahmon ibn avf")

