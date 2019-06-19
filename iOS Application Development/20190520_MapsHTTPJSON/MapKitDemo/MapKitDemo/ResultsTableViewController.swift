//
//  ResultsTableViewController.swift
//  MapKitDemo
//
//  Created by Shemar Henry on 17/06/2019.
//  Copyright © 2019 Maxim Bilan. All rights reserved.
//

import UIKit
import UIKit
import MapKit
import CoreLocation

class ResultsTableViewController: UITableViewController {

    var mapItems: [MKMapItem]?
    var myLocation: CLLocation!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //viewConfigurations()
        // Uncomment the following line to preserve selection between presentations
        // self.clearsSelectionOnViewWillAppear = false

        // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
        // self.navigationItem.rightBarButtonItem = self.editButtonItem
    }
    
    private func viewConfigurations() {
        tableView.register(UINib.init(nibName: "ResultsTableCell", bundle: nil), forCellReuseIdentifier: "result_cell")
    }

    // MARK: - Table view data source

    override func numberOfSections(in tableView: UITableView) -> Int {
        // #warning Incomplete implementation, return the number of sections
        return 1
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        return mapItems?.count ?? 0
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(
            withIdentifier: "resultCell", for: indexPath) as! ResultsTableCell

        // Configure the cell...
        let row = indexPath.row
        
        if let item = mapItems?[row] {
            cell.nameLabel.text = item.name
            let distance = self.myLocation.distance(from: item.placemark.location!)/1609.344
            let str_distance = String(distance) + " Miles"
            cell.phoneLabel.text = str_distance
            
            cell.openInMAp = {
                let regionSpan = MKCoordinateRegion(center: item.placemark.coordinate, latitudinalMeters: 1000, longitudinalMeters: 1000)
                let options = [
                    MKLaunchOptionsMapCenterKey: NSValue(mkCoordinate: regionSpan.center),
                    MKLaunchOptionsMapSpanKey: NSValue(mkCoordinateSpan: regionSpan.span)
                ]
                let mapItem = MKMapItem(placemark: item.placemark)
                mapItem.name = item.placemark.name
                mapItem.openInMaps(launchOptions: options)
            }
        }
        
        return cell
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        let routeViewController = segue.destination
            as! RouteViewController
        
        if let indexPath = self.tableView.indexPathForSelectedRow,
            let destination = mapItems?[indexPath.row] {
            routeViewController.destination = destination
        }
    }

    /*
    // Override to support conditional editing of the table view.
    override func tableView(_ tableView: UITableView, canEditRowAt indexPath: IndexPath) -> Bool {
        // Return false if you do not want the specified item to be editable.
        return true
    }
    */

    /*
    // Override to support editing the table view.
    override func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle, forRowAt indexPath: IndexPath) {
        if editingStyle == .delete {
            // Delete the row from the data source
            tableView.deleteRows(at: [indexPath], with: .fade)
        } else if editingStyle == .insert {
            // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
        }    
    }
    */

    /*
    // Override to support rearranging the table view.
    override func tableView(_ tableView: UITableView, moveRowAt fromIndexPath: IndexPath, to: IndexPath) {

    }
    */

    /*
    // Override to support conditional rearranging of the table view.
    override func tableView(_ tableView: UITableView, canMoveRowAt indexPath: IndexPath) -> Bool {
        // Return false if you do not want the item to be re-orderable.
        return true
    }
    */

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
