import UIKit
import Firebase
import FirebaseFirestore

class StoryWriterViewController: UIViewController{
    @IBOutlet weak var titleTextField: UITextField!
    @IBOutlet weak var storyView: UITextView!
    var docRef:DocumentReference!
    var metadatadocRef:DocumentReference!
    var requestDocRef:DocumentReference!
    var storyID:Int!
    var requestID:Int!
    var storyCoalition:String!
    @IBOutlet weak var eqSwitch: UISwitch!
    @IBOutlet weak var envSwitch: UISwitch!
    @IBOutlet weak var edSwitch: UISwitch!
    @IBOutlet weak var woSwitch: UISwitch!
    @IBOutlet weak var oSwitch: UISwitch!
    
    @IBAction func uploadTapped(_ sender: UIButton) {
        guard let titleText = titleTextField.text, !titleText.isEmpty else {return}
        guard let storyText = storyView.text, !storyText.isEmpty else {return}
        metadatadocRef = Firestore.firestore().document("Request/RequestMetaData")
        
        var filepath:String!
        metadatadocRef.getDocument { (DocumentSnapshot, error) in
            guard let docSnapshot = DocumentSnapshot, DocumentSnapshot?.exists ?? false else {return}
            let mydata = docSnapshot.data()
            self.storyID = mydata?["Story Count"] as? Int ?? 0
            self.requestID = mydata?["Request Count"] as? Int ?? 0
            print(self.storyID)
            self.storyID = (self.storyID) + 1
            self.requestID = (self.requestID) + 1
            filepath = "Stories/\(self.storyID)"
        }
        var metaDataToSave: [String: Any] = ["Story Count":self.storyID ?? 0, "Request Count":self.requestID ?? 0]
        metadatadocRef.updateData(metaDataToSave) {err in
            if let err = err{
                print("Error updating document")
            } else{
                print(self.storyID)
                print("Update Sucessful")
            }
        }
        requestDocRef = Firestore.firestore().document("Request/\(self.requestID ?? 0)")
        let requestToPost: [String: Any] = ["Header": "Story", "DocRef": titleText]
        requestDocRef.setData(requestToPost) { (error) in
            if let error = error{
                print(error.localizedDescription)
            } else{
                print(self.requestID)
                print("Request has been posted")
            }
        }
        docRef = Firestore.firestore().document("Stories/" + titleText)
        if(eqSwitch.isOn){
            storyCoalition = "Equality"
        }
        else if(envSwitch.isOn){
            storyCoalition = "Environment"
        }
        else if(woSwitch.isOn){
            storyCoalition = "Worker's Rights"
        }
        else if(edSwitch.isOn){
            storyCoalition = "Education"
        }
        else if(oSwitch.isOn){
            storyCoalition = "Other"
        }
        else{
            storyCoalition = "None Selected"
        }
        let dataToSave: [String: Any] = ["Author":"Tej", "Body":storyText, "Title": titleText, "Coalition_Type":storyCoalition, "Likes":0]
        docRef.setData(dataToSave) { (error) in
            if let error = error{
                print(error.localizedDescription)
            } else{
                print("Data has been saved!")
            }
            
        }
    }
    override func viewDidLoad(){
        super.viewDidLoad()

    }
}
