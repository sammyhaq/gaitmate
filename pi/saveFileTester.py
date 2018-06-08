import SaveFileHelper

def main():
    saver = SaveFileHelper.SaveFileHelper("testfile.txt");
    saver.writeData("10","20", "30");
    saver.writeData("40", "50", "60");
    saver.closeHelper();

main();
