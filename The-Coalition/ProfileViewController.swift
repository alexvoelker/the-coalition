import UIKit
import Firebase
import FirebaseFirestore
class ProfileViewController: UIViewController{
    var docRef: DocumentReference!
    @IBOutlet weak var usernameLabel:UILabel!
    @IBOutlet weak var bioLabel:UILabel!
    @IBOutlet weak var logOutButton:UIButton!
    @IBOutlet weak var makeAStoryButton:UIButton!
    @IBOutlet weak var storiesButton:UIButton!
    var metadatadocRef:DocumentReference!
    var requestDocRef:DocumentReference!
    var userDocRef:DocumentReference!
    func loadLabel(){
        docRef.getDocument { (DocumentSnapshot, error) in
            guard let docSnapshot = DocumentSnapshot, DocumentSnapshot?.exists ?? false else {return}
            let mydata = docSnapshot.data()
            let username = mydata?["Username"] as? String ?? ""
            let bio = mydata?["Bio"] as? String ?? ""
            self.usernameLabel.text = username
            self.bioLabel.text = bio
        }
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        docRef = Firestore.firestore().document("User/Avya Sharma")
        loadLabel()
    }
}
