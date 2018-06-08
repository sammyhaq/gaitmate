import LoadFileHelper
import SaveFileHelper

def main():
    print("Writing and saving test file.. ('testfile.txt')");
    saver = SaveFileHelper.SaveFileHelper("testfile.txt");
    saver.writeData("10","20", "30");
    saver.writeData("40", "50", "60");
    saver.closeHelper();
    
    loader = LoadFileHelper.LoadFileHelper("testfile.txt");
    loader.parseData();

    print("Testing getData_X()");
    print(loader.getData_X());
    print("\n");

    print("Testing getData_Y()");
    print(loader.getData_Y());
    print("\n");


    print("Testing getData_Z()");
    print(loader.getData_Z());
    print("\n");

    print("Testing getData()");
    print(loader.getData());

    print("\n");
    print("Testing Complete.");


main();
