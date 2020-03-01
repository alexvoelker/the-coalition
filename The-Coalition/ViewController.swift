//
//  ViewController.swift
//  The-Coalition
//
//  Created by Alex Voelker on 2/29/20.
//  Copyright © 2020 Coaliton of Interest Inc. All rights reserved.
//

import UIKit
import Firebase
import FirebaseFirestore
class ViewController: UIViewController {
    
    @IBOutlet weak var passwordTextField: UITextField!
    @IBOutlet weak var usernameTextField: UITextField!

    @IBOutlet weak var logInButton: UIButton!
    @IBOutlet weak var accessButton: UIButton!
    
    var userID:Int!
    var requestID:Int!
    var metadatadocRef:DocumentReference!
    var requestDocRef:DocumentReference!
    var docRef:DocumentReference!
    @IBAction func logInTapped(_ sender: Any) {
        guard let username = usernameTextField.text, !username.isEmpty else {return}
        guard let password = passwordTextField.text, !password.isEmpty else {return}
        metadatadocRef = Firestore.firestore().document("Request/RequestMetaData")
        metadatadocRef.getDocument { (DocumentSnapshot, error) in
            guard let docSnapshot = DocumentSnapshot, DocumentSnapshot?.exists ?? false else {return}
            let mydata = docSnapshot.data()
            self.userID = mydata?["User Count"] as? Int ?? 0
            self.requestID = mydata?["Request Count"] as? Int ?? 0
            print(self.userID)
            self.userID = (self.userID) + 1
            self.requestID = (self.requestID) + 1
        }
        var metaDataToSave: [String: Any] = ["User Count":self.userID ?? 0, "Request Count":self.requestID ?? 0]
        metadatadocRef.updateData(metaDataToSave) {err in
            if let err = err{
                print("Error updating document")
            } else{
                print(self.requestID)
                print("Update Sucessful")
            }
        }
        let requestToPost: [String: Any] = ["Header": "User", "DocRef": self.userID]
        requestDocRef.setData(requestToPost) { (error) in
            if let error = error{
                print(error.localizedDescription)
            } else{
                print(self.requestID)
                print("Request has been posted")
            }
        }
        let dataToSave: [String: Any] = ["Bio":"I love cookies", "CoalitionsPartof":0, "Password": password, "Stories":"None", "Username":username]
        docRef.setData(dataToSave) { (error) in
            if let error = error{
                print(error.localizedDescription)
            } else{
                print("Data has been saved!")
            }
        }
        accessButton.isHidden = false
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        print("Hi")
        accessButton.isHidden = true
        
    }

}

