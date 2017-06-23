#pragma once

module objectbox
{
    module base
    {

        interface OBElement;
        interface OBContainer;
        sequence<OBElement*> OBElements;
        sequence<string> StringSeq;

        interface OBElement
        {
            string getName();
            void setName(string name);
            string getDescription();
            void setDescription(string description);
            string getUuid();
            string getType();
            OBContainer* getParent();
            void setParent(OBContainer* parent);
            //gui element add themself to OBElement, to server it's reminder
            void registerObserver(OBElement* observer);
            void removeObserver(OBElement* observer);
            //exist as a reminder,should be not be invoked by client,invoked by itself
            void notifyObservers(string diffInfo);
            void updateBySubject(OBElement* subject, string diffInfo);
        };

        interface OBContainer extends OBElement
        {
            OBElements getChildren();
            OBElement* getOBElementByName(string path);
            OBElement* createOBElement(string name, string type);
            void removeChild(OBElement* child);
            string getOBContainerInfo();
        };

        //server should have only one OBCenter object
        //其中的OBElement应该都是Server通过程序添加进去的
        //OBElement的入口
        interface OBCenter extends OBContainer
        {

        };

        //can access inner data in server
        interface OBPythonRunner extends OBElement
        {
            string getCwd();
            void runPyFile(string pyFilePath);
        };

    };
};


