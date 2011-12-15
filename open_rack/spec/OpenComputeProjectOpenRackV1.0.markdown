latex input:        mmd-article-header
Title:              Open Compute Project Open Rack v1.0
Base Header Level:  2  
CSS:                /base.css
LaTeX Mode:         memoir  
latex input:        mmd-article-begin-doc
latex footer:       mmd-memoir-footer

![][header1]

[header1]: ../images/OCPlogo_vert.png

Open Compute Project Open Rack v1.0
==========================================================

Authors: 

<!-- \pagebreak -->
<!-- \pagestyle{fancy} -->

Scope
-----

This document describes the technical specifications for the custom rack that houses Open Compute Project server technologies.

Overview
--------

When data center design and hardware design move in concert, they can improve efficiency and reduce power consumption. To this end, the Open Compute Project is a set of technologies that reduces energy consumption and cost, increases reliability and choice in the marketplace, and simplifies operations and maintenance. One key objective is openness—the project is starting with the opening of the specifications and mechanical designs for the major components of a data center, and the efficiency results achieved at facilities using Open Compute technologies.

The main components of this project are the open rack and equipment chassis that can be configured as a server rack, storage box, and more. The open rack uses an all-encompassing design to accommodate compatible Open Compute Project chassis components, and include the power solution as well as input and output voltage distribution.

### License
As of April 7, 2011, the following persons or entities have made this Specification available under the Open Web Foundation Final Specification Agreement (OWFa 1.0), which is available at [www.openwebfoundation.org/legal/the-owf-1-0-agreements/owfa-1-0](http://www.openwebfoundation.org/legal/the-owf-1-0-agreements/owfa-1-0): 

Facebook, Inc.

You can review the signed copies of the Open Web Foundation Agreement Version 1.0 for this Specification at [opencompute.org/licensing/](http://opencompute.org/licensing/), which may also include additional parties to those listed above. 

Your use of this Specification may be subject to other third party rights. THIS SPECIFICATION IS PROVIDED "AS IS." The contributors expressly disclaim any warranties (express, implied, or otherwise), including implied warranties of merchantability, non-infringement, fitness for a particular purpose, or title, related to the Specification. The entire risk as to implementing or otherwise using the Specification is assumed by the Specification implementer and user. IN NO EVENT WILL ANY PARTY BE LIABLE TO ANY OTHER PARTY FOR LOST PROFITS OR ANY FORM OF INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES OF ANY CHARACTER FROM ANY CAUSES OF ACTION OF ANY KIND WITH RESPECT TO THIS SPECIFICATION OR ITS GOVERNING AGREEMENT, WHETHER BASED ON BREACH OF CONTRACT, TORT (INCLUDING NEGLIGENCE), OR OTHERWISE, AND WHETHER OR NOT THE OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

<a name="OpenRackOverview"></a>
Open Rack Overview
------------------

The open rack has a very flexible configuration. The rack comes in two form factors:

* Single column
* Triplet (a three column rack in a single cabinet)

The rack can be as high as 48U, but see <a href="#OptionalHeight">Optional Rack Heights</a> for more configurations.

Each column in the rack is divided into three _power zones_. A power zone comprises an equipment bay up to 12U high for the compute, storage, or other components and a power shelf up to 3U high. The _power shelf_ includes backup power capability using 48V from an external <a href="http://opencompute.org/projects/battery-cabinet/">Open Compute Project Battery Cabinet</a>, or it comprises a 1U or 2U power shelf and 1U Battery Backup Unit that embeds batteries. Each power zone is stacked one above another. The power shelf is described in <a href="#PowerShelfSpecifications">Power Shelf Specifications</a>.

Each column has space for three 1U Ethernet switches. In the current version, the switches are installed in one of two locations: 

* All three switches are at the top of the rack, above the topmost power zone.
* Each power zone has its own switch located within its equipment bay, typically above the 3U power shelf slot, so the switch may be powered at 12V from its own power zone.

Users may arrange the switches and equipment in other configurations as needed.

Each equipment bay in a power zone can be set up in various configurations and can accommodate different numbers and height of equipment chassis (such as individual server or storage chassis), as long as they add up to 12U (maximum) per power zone. Motherboards and other Open Compute hardware are hot-swappable within the individual equipment bay.

For example, the top power zone can have six 2U chassis, the middle power zone can have one 4U chassis, three 2U chassis and two 1U chassis, and the bottom power zone can have four 1.5U chassis and two 3U chassis. Each bay can be partially stuffed as well.

These varied configurations are achieved because the sidewalls of the rack enclosure can be designed to accommodate various equipment mounting configurations. For instance, the side walls may be configured with threaded holes to accommodate screws directly through a chassis/shelf wall, or flanges may be bent out of the sidewalls at the appropriate "RU" level to support equipment chassis, or the side walls may be modified to accommodate equipment made to fit another standard (such as EIA 310 19" standard). As long as the design follows Open Compute Project standards, the chassis (whether server chassis, storage chassis, or other) will fit.

### Open Rack Images and Drawings

![][fig1a]

[fig1a]: ../images/single_col_front.png "Figure 1a Open Rack Single Column (Shown with 2 Bus Bar Configuration)"

_Figure 1a Open Rack Single Column (Shown with 2 Bus Bar Configuration)_

![][fig1b]

[fig1b]: ../images/single_col_rear_2bus.png "Figure 1b Open Rack Single Column (Shown with 2 Bus Bar Configuration)"

_Figure 1a Open Rack Single Column (Shown with 2 Bus Bar Configuration)_

![][fig2a]

[fig2a]: ../images/triplet_front.png "Figure 2a Open Rack Triplet"

_Figure 2a Open Rack Triplet_

![][fig2b]

[fig2b]: ../images/triplet_rear.png "Figure 2b Open Rack Triplet"

_Figure 2b Open Rack Triplet_
 
![][fig3a]

[fig3a]: ../images/triplet_front_control_drawing.png "Figure 3a Open Rack Structural Drawing with Vertical PDUs"

![][fig3b]

[fig3b]: ../images/triplet_rear_control_drawing.png "Figure 3b Open Rack Structural Drawing with Vertical PDUs"

_Figure 3 Open Rack Structural Drawing with Vertical PDUs_

![][fig4]

[fig4]: ../images/triplet_control_drawing_hpdu.png "Figure 4 Open Rack Structural Drawing with Horizontal PDUs (Bus Bars Are Always Vertical)"

_Figure 4 Open Rack Structural Drawing with Horizontal PDUs (Bus Bars Are Always Vertical)_

<a name="OptionalHeight"></a> 
### Optional Rack Heights

The overall rack height is not a hard requirement:

* The nominal rack is 48U high, where each power zone is 12U high with a 3U power shelf.
* The rack can be made 45U high, where each power zone is 11U high with a 3U power shelf, or each power zone is 12U high with a 2U power shelf.
* The rack can be made 42U high, where each power zone is 10U high with a 3U power shelf, or each power zone is 11U high with a 2U power shelf.

The rack height can be measured in 0.5U increments, so there can be seven 1.5U servers in a 10.5U power zone, for example.

### Mechanical

Primary materials used in construction of the rack include the following:

* Cold-rolled steel in sheet form
* Zinc pre-plated cold-rolled steel in sheet form
* Plastic cabling ducts
* Each column is nominally 610mm/24" wide, which includes:
    * 38mm/1.5" x 38mm/1.5" square raw steel tubing for the frame (Open Rack single column)
    * 51mm/2" x 51mm/2" square raw steel tubing for the frame (Open Rack triplet)
    * 533mm/21" wide of usable IT space per column (valid for both the above options) 
* Rack width is 610mm/24" (Open Rack single column)
* Rack width is 1820mm/71.5" (Open Rack triplet), for ±1" tolerance in two triplets side by side
* Depth can be no shorter than 900mm/36" and no longer than 1220mm/48"

The area where the power shelf is located has these physical dimensions:

* 533mm/21" wide
* 457mm/18" deep (maximum); depth can vary depending upon the power shelf design
* 3U height (maximum); if 2U height is the total height of the power shelf and BBU, then the remaining 1U in each power zone may be removed to reduce the total height of the rack by 3U. Otherwise, the empty space must be blocked off so air doesn't flow through (see <a href="#PowerShelfSpecifications">Power Shelf Specifications</a> for details).

Refer to the CAD model for exact dimensions and details of the open rack.

The triplet rack has a minimum of 6 casters capable of supporting the specified net weight of the chassis while rolling. They are mounted in such a manner so they withstand tipping under normal deployment or relocation activity. Six leveling feet are threaded into nuts welded into the bottom of the rack.

All joining in the rack is done by welding. The raw steel tubing is welded together to form the frame. After welding, black powder coat paint is applied to the weldments.

Next, zinc plated steel panels are screwed onto the rack using threaded fasteners. The panels are installed on both outer sides and in between each column. 

One panel is installed at the top of each column; one rivet in each corner secures the panel to the top of the rack. A zinc plated panel is installed at the bottom of the rack and is held in place by rivets or screws. The top and bottom panels are baffles that close off air holes for airflow impedance.

The cabling duct is mounted to the vertical columns as needed. It allows cables to enter and exit the rack. 

The rack is shipped to an assembly facility where the electrical components are installed and network switches put into place. Server chassis (or other equipment such as storage chassis) are installed at this time. 

### Prescribed Materials

The equipment chassis is zinc-plated sheet metal. The chassis allows for the easy installation of hardware components without requiring any tools. 

### Thermal Specifications

The following table indicates the thermal specifications for the rack. 

Thermal Specification | Value                       |
--------------------- | --------------------------- |
Loading               | Idle to 100%                |
Inlet temperature     | 65°F to 85°F (18°C to 29°C) |
Humidity*             | Approximately 30 - 90%      |
Altitude              | 1000m (~ 3300ft)            |
Dew point*            | 41.9ºF minimum (5.5°C)      |

_Figure 5 Thermal Specifications at Rack Level_

*Based on regional climate conditions where the data center operates; supply air temperature 64.4°F to 80.6°F (18°C to 27°C), relative humidity 65% maximum, dew point 41.9°F to 59°F). For more information, including a psychrometric chart, see the Open Compute Project Data Center v1.0 specification.

<a name="PowerShelfSpecifications"></a>
Power Shelf Specifications
--------------------------

The rack is powered with three-phase (nominal range 340Vac – 480Vac RMS) with a single-phase Line-to-Neutral distribution to each power zone. In the US, the open rack will use 480Vac three-phase with a single-phase 277Vac distribution to each power zone. The power shelf is a single-phase power converter rated 200–277Vac nominal, and supports a voltage range from 180Vac to 290Vac for worldwide compatibility. 

**Note:** The power shelf can also be powered by a true three-phase input voltage, with or without a Neutral conductor; refer to <a href="PDUSpecs">PDU Specifications for more information</a>. 

The power solution must support redundancy, no matter which input voltage configuration is used and regardless of how much space it occupies in the power zone.

Each column contains three power shelves. Each power shelf supports up to ~ 6KW at 12Vdc (or 12.5Vdc) output, for a maximum of 20KVA of AC power (277Vac x 24A x 3 phases) in a single column when using a US standard NEMA L22-30P plug. The AC plugs are normally derated 20%; the L22-30P becomes a 24A plug. These ratings factor in an efficiency of ~ 0.94 for an Open Compute Project power supply module (for example, 4.2KW = 277Vac x 16A x 0.94 efficiency) and nearly unity power factor (PF) at full load. Higher power than 20KVA per column may be achieved by hard wiring the AC power cord to the grid or by using a higher power industrial plug. The power shelf needs a correspondingly increased power rating in this case.

![][fig6]

[fig6]: ../images/triplet_front_section.png "Figure 6 Power Zone in a Triplet (3U Power Shelf, 12.5V, 4.2KW Power, L22-20P Plug Shown)"

_Figure 6 Power Zone in a Triplet (3U Power Shelf, 12.5V, 4.2KW Power, L22-20P Plug Shown)_

The rack uses three-phase power for flexibility and cost effectiveness. Each column in a triplet gets one phase for each power zone (when using a vertical PDU), or each column gets its own phase (when using a horizontal PDU). For either configuration, the three-phase balance needs to be guaranteed (phase balance is required as much as possible):

* When using a vertical PDU (for single column rack or triplet rack), each of the three power zones must be configured identically to the other two. 
* When using a horizontal PDU in a triplet, the configuration for a given column is flexible (as described <a href="#OpenRackOverview">Open Rack Overview</a>), as long as the two remaining columns are configured identically.
For both single-column racks and triplet racks, each of the three PDUs has its own plug. Both types of racks use one of these AC three-phase plugs in the US, depending upon the level of power desired:
* L22-20P plug: Rated 20A per column, it becomes a 16A plug after the 20% derating, (up to 13.3KVA of AC power per column). 
* NEMA L22-30P plug: Rated 30A per column, it becomes a 16A plug after the 20% derating (up to 20KVA of AC power per column). 

The open rack supports backup power functionality, with no interruption of service in case of an AC outage. When the Open Compute Project battery cabinet is used, the 48Vdc backup voltage is connected to the Open Compute V1 power shelf (see <a href="#PowerShelfBatteryBackupOptions">Power Shelf and Battery Backup Options</a> below) by means of high-current blade connectors APP SB175 (one connector supports three power zones). 

The use of 200Vac instead of 277Vac requires a 30A plug (it supports 24A after the 20% derating) to get to a similar power level achievable by an L22-20P plug in the US. The maximum usable DC power at 12.5V for each power zone when powered at 200Vac would be ~ 4.5KW (200Vac x 24A x 0.94 efficiency), and nearly unity power factor at full load.

![][fig7]

[fig7]: ../images/triplet_rear_hpdu_annotated.png  "Figure 7 Open Rack Triplet Rear View"

_Figure 7 Open Rack Triplet Rear View_

Each triplet has 9 power zones (three in each column), and three PDUs (either vertical or horizontal). A single-column rack has 3 power zones with one vertical AC PDU when the Open Compute Project battery cabinet is not used, or with two vertical PDUs (one AC and one DC) when the cabinet is used. The PDUs are described in greater detail in <a href="#PDUSpecs">PDU Specifications</a>.

The chassis are hot swapped from the front of the rack. It uses nominal 12V from the bus bars installed at the rear of each power zone, although the suggested voltage is 12.5V. The bus bars can be adjusted for higher current, depending on the desired power per column, as they are interchangeable. In addition, the bus bars can be configured in various ways in the power zone:

* Two pairs (+/-) of bus bars, on the left and right sides of the column
* Three pairs (+/-) of bus bars, on the left, right and middle of the column
* One pair (+/-) of bus bars, down the center of the column

The best configuration to choose depends on the nature of the application or rack configuration. Note that the centered bus bar is able to deliver the full power available in the power zone.

A third optional centered bus bar can be installed also, allowing the deployment of highly dense configurations (for example, when installing three 7" wide motherboards in each slot). In this case the total height of the rack may be reduced since the maximum AC power per column is capped anyway. 

The 12V output of each power zone is independent and floating with respect to the other power zones. This helps reduce potential DC currents from looping through the rack, and against onset noise. The two bus bars on the right and left side can support up to 240A each, while the optional centered bus bar can support up to the full 336A (this example is valid for a V1 power shelf rated 4.2KW at 12.5V).

<a name="PowerShelfBatteryBackupOptions"></a>
### Power Shelf and Battery Backup Options
Backup power is provided by one of two power shelf configurations: 

**V1 power shelf:** This (6 + 1) redundant shelf is 3U high and requires the Open Compute Project battery cabinet to engage backup functions. The power modules deployed in this shelf are a variation of the Open Compute Project power supply with increased power, repackaged as a hot swappable module with handle, and adding more features like a power module failure signal and OR-ing devices. The opto-isolated failure signals are daisy-chained between all three power shelves in each column to allow for reporting of a power module failure, identifying the shelf where the failure occurred. The failure is reported to the management switch through a custom digital box sitting on top of the rack, with one Ethernet RJ45 output and several inputs.

One Open Compute Project battery cabinet sits in between a pair of triplets in the data center aisle, providing 48V DC backup voltage used in the event of an AC power outage. The cabinet is normally offline and exceeds 99.75% of equivalent UPS efficiency. For more information, see the <a href="http://opencompute.org/projects/battery-cabinet/">Open Compute Project Battery Cabinet Hardware v1.0 specification</a>.

![][fig8]

[fig8]: ../images/v1_power_shelf.png "Figure 8 Open Rack Triplet with 9 V1 Power Shelves (3U) and hPDUs (OCP Battery Cabinet Not Shown)"
 
_Figure 8 Open Rack Triplet with 9 V1 Power Shelves (3U) and hPDUs (OCP Battery Cabinet Not Shown)_

**V2 power shelf:** This (N + 1) redundant shelf is 2U (or 1U) high with a 1U battery backup unit (BBU) module normally installed underneath. The Open Compute Project battery cabinet is not needed as the BBU normally includes its own high-density lithium-ion battery pack. Each BBU module may also be placed above the 2U/1U power shelf to directly power the bus bar behind it (depending on topology).
To account for power module failure signals and more functionality, a digital bus with a more complete reporting on the power shelf functionality and health may be defined as needed for the V2 power solution.

![][fig9]

[fig9]: ../images/v2_power_shelf.png "9 Open Rack Triplet with 2U Power Shelf and 1U BBU (Optional 12.5V Bus Bar Shown)"
_Figure 9 Open Rack Triplet with 2U Power Shelf and 1U BBU (Optional 12.5V Bus Bar Shown)_

### DC Input Voltage Options
The open rack triplet may be powered by High Voltage DC input (HVDC) instead.

The power shelf, after some customizations (such as input connector, circuitry adjustment, safety and regulatory compliance, and so forth), may be able to use DC input directly. Otherwise a custom power shelf can be designed for DC input only. Typical voltage levels are in the range of 380Vdc ~ 400Vdc. This option gives the ability to power the rack in a data center environment with HVDC distribution or when the DC power is generated on site (for example, by fuel cell or other renewable energy source). 

In this case, the PDUs must be customized accordingly. The BBU scheme normally integrated into the rack may or may not be necessary anymore.

<a name="PDUSpecs"></a>
PDU Specifications
------------------

If the V1 power shelf is used in a single-column rack, two vertical PDUs are needed: one AC and one DC. If the rack uses a V2 power shelf, then only the AC PDU is needed.

Each triplet with V1 power shelves has three PDUs (either vertical or horizontal) that distribute both AC and DC. A triplet with V2 power shelves has three PDUs (either vertical or horizontal) that distribute only AC. 

![][fig10]

[fig10]: ../images/triplet_rear_vpdu.png "Figure 10 Triplet Rack with vPDUs"

_Figure 10 Triplet Rack with vPDUs_

Vertical PDUs (vPDUs) are preferred to horizontal PDUs (hPDUs) in the triplet to avoid partial shutdown of the whole logical rack in the event that one hPDU fails, meaning 1/3 of each logical column would shut down. However, if a vPDU fails, only the column powered by that vPDU is affected, so just one whole logical column would shut down on the triplet. Normally it is more acceptable to lose one logical column than 1/3 of each of three logical columns; however, it depends on the actual physical configuration -- how the switches are routed to the chassis in the triplet.

It should be noted that, with hPDUs, there is single-phase Line to Neutral AC voltage distribution for each column, while with vPDUs, there is single-phase Line to Neutral AC voltage distribution for each power zone in the same column.
 
![][fig11]

[fig11]: ../images/triplet_rear_hpdu.png "Figure 11 Triplet Rack with hPDUs"

_Figure 11 Triplet Rack with hPDUs_

### Suggested PDU Dimensions and Configurations
The vPDU for a triplet rack is 2" wide, to match the square tubing of the rack, and up to 4" deep (AC and DC distribution in the same PDU) or 2" deep (AC distribution only). 

The vPDU for a single-column rack is 1.5" square to match the square tubing of the rack (AC or DC distribution only in each PDU), and up to 2” deep. 

The hPDU for a triplet rack is 1U high, and up to 4" deep (AC and DC distribution in the same PDU) or 2" deep (AC distribution only). 

PDU height correlates to the triplet height for the vPDU version, and to the triplet width for hPDU version (both the triplet and the PDU are 71.5" wide). 

For the single-column rack or for each column in a triplet with a vPDU, the AC voltage distribution is as follows:

* Power zone 1 is powered by 277V Line 1 to Neutral
* Power zone 2 is powered by 277V Line 2 to Neutral 
* Power zone 3 is powered by 277V Line 3 to Neutral 

For the first column in a triplet with an hPDU, the AC voltage distribution is as follows:

* Power zone 1 is powered by 277V Line 1 to Neutral
* Power zone 2 is powered by 277V Line 1 to Neutral 
* Power zone 3 is powered by 277V Line 1 to Neutral 

The second and third columns in the triplet are powered by the remaining two phases (Line 2 to Neutral and Line 3 to Neutral respectively).

The 277V value always refers to the usage in the US, with three-phase power at 480Vac. 

For a power shelf solution using true three-phase power with or without Neutral, the AC PDU would distribute the same identical three-phase voltage to every power zone (4 or 5 wires, including GND conductor). Therefore a three-phase solution at the power shelf level is another option. This approach makes more sense when a high power density solution is needed, and in this way a three-phase balance is easily achieved without regard to the configuration of the load in the power zones. It also avoids usage of the Neutral conductor. However, a three-phase solution at the power shelf level that includes the Neutral conductor may still be considered, and while there is no longer an easy three-phase balance, it has other advantages.

In general, all the PDUs are installed at the rear of the rack.

Only hPDUs are perforated for air exhaust. AC and/or DC outputs from the PDUs are normally dongle cables terminated with connectors (that must use strain relief or molding), and with the corresponding counterparts installed in the rear panel of the power shelf. 

Conclusion
----------

This specification is a work in progress. To offer feedback or contribute, join the mailing list at [lists.opencompute.com/mailman/listinfo/opencompute-openrack](http://lists.opencompute.com/mailman/listinfo/opencompute-openrack).
