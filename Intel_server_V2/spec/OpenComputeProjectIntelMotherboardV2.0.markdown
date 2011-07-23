latex input:        mmd-article-header
Title:              Open Compute Project Intel Motherboard Hardware v2.0
Base Header Level:  2  
CSS:                /base.css
LaTeX Mode:         memoir  
latex input:        mmd-article-begin-doc
latex footer:       mmd-memoir-footer

![][header1]

[header1]: ../images/OCPlogo_vert.png

Open Compute Project Intel Motherboard Hardware v2.0
==========================================================

Author: Harry Li, Engineer

Author: Amir Michael, Engineer

<!-- \pagebreak -->
<!-- \pagestyle{fancy} -->

Scope
-----
This document defines the technical specifications for the Intel motherboard used in Open Compute servers.

Contents
--------

<!--  \tableofcontents -->

Overview
--------
When data center design and hardware design move in concert, they can improve efficiency and reduce power consumption. To this end, the Open Compute Project is a set of technologies that reduces energy consumption and cost, increases reliability and choice in the marketplace, and simplifies operations and maintenance. One key objective is openness—the project is starting with the opening of the specifications and mechanical designs for the major components of a data center, and the efficiency results achieved at facilities using Open Compute technologies.

One component of this project is a custom motherboard. This document describes both Open Compute Project Intel motherboards: the Intel entry board and the Intel efficient performance board. The motherboard is power-optimized and barebones, designed to provide the lowest capital and operating costs. Many features found in traditional motherboards have been removed from the design.

### License
As of April 7, 2011, the following persons or entities have made this Specification available under the Open Web Foundation Agreement Version 1.0, which is available at [www.openwebfoundation.org/draft-agreements/draft---owfa-v-1-0](http://www.openwebfoundation.org/draft-agreements/draft---owfa-v-1-0 "OpenWeb Foundation License")

Facebook, Inc.

You can review the signed copies of the Open Web Foundation Agreement Version 1.0 for this Specification at [TBD], which may also include additional parties to those listed above.

Your use of this Specification may be subject to other third party rights. THIS SPECIFICATION IS PROVIDED "AS IS." The contributors expressly disclaim any warranties (express, implied, or otherwise), including implied warranties of merchantability, non-infringement, fitness for a particular purpose, or title, related to the Specification. The entire risk as to implementing or otherwise using the Specification is assumed by the Specification implementer and user. IN NO EVENT WILL ANY PARTY BE LIABLE TO ANY OTHER PARTY FOR LOST PROFITS OR ANY FORM OF INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES OF ANY CHARACTER FROM ANY CAUSES OF ACTION OF ANY KIND WITH RESPECT TO THIS SPECIFICATION OR ITS GOVERNING AGREEMENT, WHETHER BASED ON BREACH OF CONTRACT, TORT (INCLUDING NEGLIGENCE), OR OTHERWISE, AND WHETHER OR NOT THE OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

### CAD Models
The following CAD files are incorporated by reference as if fully set forth in this specification:

* TBD


Entry Motherboard Features
--------------------
### Block Diagram

Figure 1 illustrates the functional block diagram of the entry motherboard.

![][fig1]

[fig1]: ../images/intel_en_block.png "Figure 1 Functional Block Diagram"

_Figure 1 Functional Block Diagram_

### Placement and Form Factor

The motherboard's form factor is 6.5x20 inches. Figure 2 illustrates board placement. The placement shows the relative positions of key components, while exact dimension and position information is available in the mechanical DXF file. The ODM should strictly follow the form factor, PCIe slot position, front IO port positions, PCIe mezzanine card connector position, power connector, and mounting holes, while other components can be shifted based on layout routing as long as relative position is maintained. As shown in Figure 25, one Open Compute chassis accommodates two motherboards. In order to remove and install one board without affecting the other board, the following internal connectors are placed as close as possible to front of the board in order to have easy frontal access:

* One vertical SATA signal connector and one SATA power connector.
* Debug card header.

![][fig2]

[fig2]: ../images/intel_en_placement.png "Figure 2 Entry Board Board Placement"

_Figure 2 Entry Board Board Placement_

### CPU and Memory

The motherboard uses next generation Intel&reg; Xeon&reg; processors. It supports these features:

* 2 Intel&reg; processors
* One full-width Intel QuickPath interconnect (QPI) link
* Single Processor Mode
* DDR3 direct attached memory support on cpu0 and cpu1

### Platform Controller Hub

The entry board uses the next generation Intel® platform controller hub (PCH), which supports the following features:

* USB ports
* Serial attached SCSI ports
* SPI interface
* SMBUS interface (master and slave)

<a name="ENPCB"></a>
###	PCB Stackup

The entry board's PCB stackup and impedance control are defined in the following tables.

Layer | Plane Description  | | Copper (oz) | Thickness (mil) | Dielectric (er) |
----- | -----------------    | ----------- | --------------- | --------------- |
      |      | Solder Mask   |             | 0.5             | 3.8             |
L1    | TOP	 | Signal        | 0.5+1.0     | 1.9             |                 |
      |      | PrePreg		 |             | 2.7             | 3.5             |
L2    | GND1 | Ground        | 2.0         | 2.6             |                 |
      |      | Core          |             | 4.0             | 3.7             |
L3    | IN1  | Signal        | 1.0         | 1.3             |                 |
      |      | PrePreg       |             | 25.0            | 4.4             |
L4    | VCC1 | Power         | 2.0         | 2.6             |                 |
      |      | Core          |             | 4.0             | 4.1             |
L5    | VCC2 | Power         | 2.0         | 2.6             |                 |
      |      | PrePreg       |             | 25.0            | 4.4             |
L6    | IN2  | Signal        | 1.0         | 1.3             |                 |
      |      | Core          |             | 4.0             | 3.7             |
L7    | GND2 | Ground        | 2.0         | 2.6             |                 |
      |      | PrePreg		 |             | 2.7             | 3.5             |
L8    | BOT  | Signal        | 0.5+1.0     | 1.9             |                 |
      |      | Solder Mask   |             | 0.5             | 3.8             |
      |      | Total         |             | 85.2            | Tolerance: +/-8mil |
[Figure 3 Entry Board PCB Stackup]


Trace Width (mil) | Air Gap Spacing (mil) | Impedance Type | Layer | Impedance Target (ohm) | Tolerance (+/- %) |
----------------- | --------------------- | -------------- | ----- | ---------------------- | ----------------- |
4.0               |	                      | Single         | 1,8   | 50                     | 15.0              |
6.5               |	                      | Single         | 1,8   | 40                     | 15.0              |
5.0               |	                      | Single         | 1,8   | 43                     | 15.0              |
3.9               | 4.1                   | Differential   | 1,8   | 83                     | 17.5              |
3.8               | 8.2                   | Differential   | 1,8   | 95                     | 17.5              |
5.0               | 7.0                   | Differential   | 1,8   | 85                     | 17.5              |
4.0               |	                      | Single         | 3,6   | 53                     | 10.0              |
6.5               |	                      | Single         | 3,6   | 50                     | 10.0              |
5.0               |	                      | Single         | 3,6   | 48                     | 10.0              |
8.0               |	                      | Single         | 3,6   | 38                     | 10.0              |
3.9               | 4.1                   | Differential   | 3,6   | 85                     | 12.0              |
3.8               | 9.1                   | Differential   | 3,6   | 95                     | 12.0              |
5.0               | 6.5                   | Differential   | 3,6   | 85                     | 12.0              |
[Figure 4 Entry Board PCB Impedance Control]


Efficient Performance Motherboard Features
--------------------
### Block Diagram

Figure 5 illustrates the functional block diagram of the efficient performance motherboard.

![][fig5]

[fig5]: ../images/intel_ep_block.png "Figure 1 Functional Block Diagram"

_Figure 1 Functional Block Diagram_

### Placement and Form Factor

The motherboard's form factor is 6.5x20 inches. Figure 6 illustrates board placement. The placement shows the relative positions of key components, while exact dimension and position information is available in the mechanical DXF file. Form factor, PCIe slot position, front IO port positions, PCIe mezzanine card connector position, power connector, and mounting holes should be followed strictly, while other components can be shifted based on layout routing as long as relative position is maintained. As shown in Figure 25, one Open Compute chassis accommodates two motherboards. In order to remove and install one board without affecting the other board, the following internal connectors are placed as close as possible to front of the board in order to have easy frontal access:

* One vertical SATA signal connector and one SATA power connector.
* Debug card header.

![][fig6]

[fig6]: ../images/intel_ep_placement.png "Figure 6 Efficient Performance Board Placement"

_Figure 6 Efficient Performance Board Placement_

### CPU and Memory

The motherboard uses next generation Intel&reg; Xeon&reg; processors. It supports these features:

* 2 Intel&reg; processors
* Single Processor Mode
* DDR3 direct attached memory support on cpu0 and cpu1

### Platform Controller Hub

The efficient performance board uses the next generation Intel® platform controller hub (PCH), which supports the following features:

* USB ports
* Serial attached SCSI ports
* SPI interface
* SMBUS interface (master and slave)

<a name="EPPCB"></a>
###	PCB Stackup 

The efficient performance board's PCB stackup and impedance control are defined in the following tables.

Layer | Plane Description  | | Copper (oz) | Thickness (mil) | Dielectric (er)    |
----- | -----------------    | ----------- | --------------- | ------------------ |
      |      | Solder Mask   |             | 0.5             | 3.8                |
L1    | TOP	 | Signal        | 0.5+1.0     | 1.9             |                    |
      |      | PrePreg		 |             | 2.7             | 3.5                |
L2    | GND1 | Ground        | 1.0         | 1.3             |                    |
      |      | Core          |             | 4.0             | 3.6                |
L3    | IN1  | Signal        | 1.0         | 1.3             |                    |
      |      | PrePreg       |             | 7.7             | 4.0                |
L4    | GND2 | Ground        | 1.0         | 1.3             |                    |
      |      | Core          |             | 4.0             | 3.6                |
L5    | IN2  | Signal        | 1.0         | 1.3             |                    |
      |      | PreReg        |             | 12.0            | 4.3                |
L6    | VCC1 | Power         | 2.0         | 2.6             |                    |
      |      | Core          |             | 4.0             | 3.6                |
L7    | VCC2 | Power         | 2.0         | 2.6             |                    |
      |      | PrePreg       |             | 12.0            | 4.3                |
L8    | IN3  | Signal        | 1.0         | 1.3             |                    |
      |      | Core          |             | 4.0             | 3.6                |
L9    | GND3 | Ground        | 1.0         | 1.3             |                    |
      |      | PrePreg		 |             | 7.7             | 4.0                |
L10   | IN4  | Signal        | 1.0         | 1.3             |                    |
      |      | Core          |             | 4.0             | 3.6                |
L11   | GND4 | Ground        | 1.0         | 1.3             |                    |
      |      | PreReg        |             | 2.7             | 3.5                |
      |      | Solder Mask   |             | 0.5             | 3.8                |
      |      | Total         |             | 85.2            | Tolerance: +/-8mil |
[Figure 7 Efficient Performance Board PCB Stackup]


Trace Width (mil) | Air Gap Spacing (mil) | Impedance Type | Layer    | Impedance Target (ohm) | Tolerance (+/- %) |
----------------- | --------------------- | -------------- | -------- | ---------------------- | ----------------- |
4.0               |	                      | Single         | 1,12     | 50                     | 15.0              |
6.5               |	                      | Single         | 1,12     | 40                     | 15.0              |
5.0               |	                      | Single         | 1,12     | 43                     | 15.0              |
3.9               | 4.1                   | Differential   | 1,12     | 83                     | 17.5              |
3.8               | 8.2                   | Differential   | 1,12     | 95                     | 17.5              |
5.0               | 7.0                   | Differential   | 1,12     | 85                     | 17.5              |
4.1               | 13                    | Differential   | 1,12     | 100                    | 10                |
4.0               |	                      | Single         | 3,5,8,10 | 53                     | 10.0              |
4.5               |	                      | Single         | 3,5,8,10 | 50                     | 10.0              |
5.0               |	                      | Single         | 3,5,8,10 | 48                     | 10.0              |
8.0               |	                      | Single         | 3,5,8,10 | 38                     | 10.0              |
3.9               | 4.1                   | Differential   | 3,5,8,10 | 85                     | 12.0              |
4.4               | 9.1                   | Differential   | 3,5,8,10 | 95                     | 12.0              |
5.0               | 6.5                   | Differential   | 3,5,8,10 | 85                     | 12.0              |
4.1               | 13                    | Differential   | 3,5,8,10 | 100                    | 10.0              |
[Figure 8 Efficient Performance Board PCB Impedance Control]

BIOS
----

The ODM is responsible for supplying and customizing a BIOS for the motherboard. The specific BIOS requirements are outlined in this section. 

### BIOS Interface and Size
The BIOS chip uses the platform controller hub's SPI interface. The ODM is responsible for selecting a specific BIOS chip that meets the required functionality. 16MB of space should be allocated for both the BIOS and the PCH management engine.

### BIOS Socket

A socket on the motherboard must be used to mount the BIOS chip to ensure that the BIOS chip can be replaced manually. The BIOS socket is easily accessible; other components on the motherboard do not interfere with the insertion or removal of the BIOS chip. A DIP-type BIOS chip and compatible socket are used for easy insertion and removal.

### BIOS Source Code
The BIOS source code comes from AMI EFI. The ODM is responsible for maintaining the BIOS source code to make sure it has the latest version from AMI and Intel.

### BIOS Configuration and Features
The BIOS is tuned to minimize system power consumption. It has the following features:

* Unused devices disabled, including PCIe lanes, PCI lanes, USB ports, SATA/SAS ports
* Tuning CPU/chipset settings to reach minimized power consumption and best performance
* SPECpower is used as guidance for ODM to validate BIOS tuning results

### BIOS Setup Menu
The ODM must provide a BIOS specification, which includes the complete BIOS, setup menu, and default settings. The setup menu allows its options to be configured before the operating system loads. The configuration options available through the boot menu include the following:

* Settings to adjust memory speed, QPI speed, Speed-step/Turbo mode, and CPU Cx power state.
* Setting for power feature after AC failure, default is set to power on.
* Settings for console redirection: 
    * **PCH Virtual COM port:** With baud rate 115200, no flow control, and terminal type VT100. 
    * **SIO COM1:** With baud rate 57600, no flow control and terminal type VT100. 
    * **Auto:** The PCH virtual COM port is enabled by default. The BIOS switches to SIO COM1 automatically, depending on hardware strapping. Default option is "Auto".
* Setting for fan speed control (for SIO FSC enabled board only).
* Setting for altitude of server deployment location.
* Hardware health monitoring display.
* Setting for watchdog timer. Default is enabled and timeout value is 15 minutes.
* Event log viewing and clearing.
* Setting for ECC error threshold, available settings are 1, 4, 10, and 1000.
* If a CMOS checksum error occurs (for example, caused by BIOS update), the BIOS loads the system default automatically after displaying a message in the console for 5 seconds and rebooting the system to apply the update without waiting for user input.
* Setting to disable all "wait for keyboard input to continue" types of features.

### PXE Boot
The BIOS supports Intel PXE boot. When PXE booting, the system first attempts to boot from the first Ethernet interface (eth0). If a PXE boot on the first Ethernet interface fails, the BIOS attempts to PXE boot from the second Ethernet interface (eth1). 

### Other Boot Options
The BIOS also supports booting from SATA/SAS and USB interfaces. The BIOS provides the capability to select boot options.

### Remote BIOS Update
The BIOS can be updated remotely under these scenarios:

* Scenario 1: Sample/Audit BIOS settings
    * Return current BIOS settings, or
    * Save/export BIOS settings in a human-readable form that can be restored/imported (as in scenario 2)
* Scenario 2: Update BIOS with pre-configured set of BIOS settings
    * Update/change multiple BIOS settings
    * Reboot
* Scenario 3: BIOS/firmware update with a new revision
    * Load new BIOS/firmware on machine and update, retaining current BIOS settings
    * Reboot

Additionally, the update tools have the following capabilities:

* Update from the operating system over the LAN – the OS standard is CentOS v5.2
* Can complete BIOS update or setup change with a single reboot (no PXE boot, no multiple reboots)
* No user interaction (like prompts)
* BIOS updates and option changes do not take longer than five minutes to complete
* Can be scripted and propagated to multiple machines

### Event Log 
An event log is available through SMBIOS. 
Per SMBIOS specification Rev 2.6, the BIOS implements SMBIOS type 15 for an event log; the assigned area is large enough to hold more than 500 event records (assuming the maximum event record length is 24 bytes, then the size will be larger than 12KB), and follow the SMBIOS event log organization format for the event log. 

The ODM must provide a system access interface and application software to retrieve and clear the event log from the BIOS, including, at minimum, a Linux application for the CentOS operating system and driver as needed. The event log must be retrieved and stored as a readable text file that is easy to handle by a scripting language under Linux. Each event record includes enhanced information identifying the error source device's vendor ID and device ID.

#### Logged Errors

* **CPU/Memory errors:** Both correctable ECC and uncorrectable ECC errors should be logged into the event log. Error categories include DRAM, Link, and L3 cache.
* **QPI errors:** Any errors that have a status register should be logged into the event log. Fatal or non-fatal classification follows the chipset vendor's recommendation.
* **PCIe errors:** Any errors that have a status register should be logged into the event log, including root complex, endpoint device, and any switch upstream/downstream ports if available. Link disable on errors should also be logged. Fatal, non-fatal, or correctable classification follows the chipset vendor's recommendation.
* **POST errors:** All POST errors detected by the BIOS during POST are logged into the event log.
* **Power errors:** Two power errors are logged:
    * 12.5V DC input power failure that causes all power rails on motherboard to lose power, including standby power.
    * Unexpected system shutdown during system S0/S1 while 12.5V DC input is still valid.

#### Error Threshold Settings
An error threshold setting must be enabled for both correctable and uncorrectable errors. Once the programmed threshold is reached, an event should be triggered and logged.

* **Memory Correctable ECC:** The threshold value is 1000. When the threshold is reached, the BIOS should log the event including DIMM location information and output DIMM location code through the debug card.
* **QPI errors:** Follow the chipset vendor's suggestion.
* **PCIe errors:** Follow the chipset vendor's suggestion.

#### BIOS Error Codes
MRC fatal error codes should be enabled for POST code output. The major and minor codes alternately display.

Hardware Monitoring
-------------------

The motherboard does not employ a traditional out of band monitoring solution. The ODM needs to provide a system access interface and application to retrieve hardware monitoring sensor readings. Lm\_sensors is the preferred tool for hardware monitoring under Linux; the ODM ensures Lm\_sensors works. The sensors to be read include voltage, temperature, and fan speed.
The NCT6681 serves as both the super IO (SIO) and hardware monitor.

### Thermal Sensors
The motherboard has five thermal sensors:

* Two to monitor temperatures for CPU0 and CPU1, retrieved through the CPU's temperature sensor interface (PECI)
* PCH temperature, retrieved through the Intel® controller hub's internal DTS, through PCH SMLink1
* Inlet temperature, retrieved through the thermistor, and located in the front of the motherboard
* Outlet temperature, retrieved through the thermistor, and located in the rear of the motherboard

The sensors should make sure that no CPU throttling is triggered due to thermal issues, under the following environmental conditions:

* Inlet temperature lower than 30C (including 30C), and 0 inch H2O pressure
* Inlet temperature higher than 30C but lower than 35C (including 35C), and 0.01 inch H2O pressure

The sensors should make sure that the total airflow rate for the chassis is lower than 89CFM, including PSU.

In the event that one fan fails, an inlet temperature of 30C with 0 inch H2O pressure environment is used to verify thermal sensors.

### Fan Connection
The motherboard has fan tachometers and PWM connections to two system fans through the midplane. See [Fan Connectors][].

### Fan Control Algorithm
The motherboard supports auto fan speed control for the system fans connected to it. The ODM must provide an optimized fan control algorithm based on the thermal solution of the system including fan, heat sink, and air duct. Fan speed control should set system fans running at lowest speed and provide enough damping to avoid speed vibration.

Midplane
--------

The midplane is a PCB that functions as a bridge between the system fans, power supply (PSU), and both motherboards. Its form factor is 2x13 inches. 

### PSU Connector

The midplane has one FCI 51939-582 male right angle header, which is mated directly with the PSU for 12.5VDC input. Figure 9 shows the pin definition and direction based on the PSU.

Pin #  | Signal        | Direction | Description                | Usage                   |
------ | ------------- | --------- | -------------------------- | ----------------------- |
P1, P2 | P12V          | Power	   | 12.5VDC                    | 12.5VDC                 |
P3, P4 | GND           | Power	   | Ground                     | Ground                  |
A1     | AUX_RTN_GND   |           | Signal return              | NC                      |
A2     | BACKUP_N      | Output	   | PSU backup mode indication | NC                      |
B1     | SHARE\_SEL_1  | Input	   | PSU mode selection	        | NC                      |
B2     | SHARE\_SEL_2  | Input	   | PSU mode selection         | NC                      |
C1     | GREEN\_LED_N  | Output	   | Low active                 | Connect to bi-color LED |
C2     | YELLOW\_LED_N | Output	   | Low active                 | Connect to bi-color LED |
D1     | RED\_LED_N    | Output	   | Low active                 | Connect to LED          |
D2     | P5V_AUX       | Power	   | 5V for LED, 50mA limited   | LED power               |
[Figure 9 Midplane to PSU Connector Pin Definition]

For the PSU LED, the midplane provides a 4-pin vertically shrouded 2.54mm pitch header with latch. This allows an LED cable to extend the PSU LED to the chassis front. The PSU connector pins C1 and C2 connect to one bi-color (green/yellow) LED with a common anode. Pin D1 is connected to one red LED. Pin D2 is 5V and used for an LED anode. Both are 3mm LEDs. A current limit resistor is required for each LED signal.

Pin | Description  |
--- | ------------ |
1   | GREEN_LED_N  |
2   | YELLOW_LED_N |
3   | RED_LED_N    |
4   | P5V_AUX      |
[Figure 10 PSU LED Header Pin Definition]

When the PSU's red LED blinks (at 1Hz, 50% duty-cycle), it indicates a PSU fan failure. 

### Fan Connectors

The midplane has connectors for the four system fans. The connector signals comply both mechanically and electrically with the specifications defined in the 4-Wire Pulse Width Modulation (PWM) Controlled Fans Specification Revision 1.3 September 2005 published by Intel Corporation. Each fan is driven by a dedicated PWM signal. Figure 11 defines the proper pin out of the connector.

Pin | Description |
--- | ----------- |
1   | GND         |
2   | 12VDC       |
3   | Sense       |
4   | Control     |
[Figure 11 Fan Header Pin-out]

A fan tachometer signal from each fan is routed to acquire fan speed. The midplane directly delivers 12.5V power to the fan connector. If one motherboard is not powered on, then its two corresponding fans are turned off to save power.

### Motherboard Connectors

The midplane has two FCI 51770-044 female right-angle power/signal connectors (2P+16S+2P: 4 power blades and 16 signals). The motherboard -- with the mated FCI 51730-162 male right angle header -- slides in and mates with one of the FCI headers on the midplane. Figure 12 shows the pin definition of the 2P+16S+2P connector; the direction is based on the midplane.

Pin #          | Signals        | Direction    | Description                                      |
-------------- | -------------- | ------------ | ------------------------------------------------ |
P1, P2         | P12V           | Power        | 12.5VDC                                          |
P3, P4         | GND            | Power        | Ground                                           |
A1             | SMB\_ALT_N     | Output       | SMBUS alert signal from hot-swap controller      |
A2             | TACH1A         | Output       | Reserved for extra fan tachometer on FAN1        |
A3             | TACH2A         | Output       | Reserved for extra fan tachometer on FAN2        |
A4             | RSVD           |              | Reserved for future                              |
B1             | SCLK           | Bi-direction | SMBUS CLOCK                                      |
B2             | SDATA          | Bi-direction | SMBUS DATA                                       |
B3             | MB_ON          | Input        | Indicates that motherboard starts powered on     |
B4             | PSU_PG         | Output       | Indicates that PSU 12.5VDC output is ready       |
C1             | FAN1_TACH      | Output       | System fan #1 tachometer                         |
C2             | FAN1_PWM       | Input        | System fan #1 PWM                                |
C3             | FAN2_TACH      | Output       | System fan #2 tachometer                         |
C4             | FAN2_PWM       | Input        | System fan #2 PWM                                |
D1 (short pin) | MATED_N        | Input        | Low active, indicates motherboard is fully mated |
D2             | MATED\_GND_RTN |              | Connected to GND in midplane                     |
D3             | MB_ID          | Output       | Motherboard ID = 0 (left), 1 (right)             |
D4             | FAN\_FAIL_N    | Output       | PSU fan failure detected                         |
[Figure 12 Midplane to Motherboard Connector Pin Definition]

### Motherboard Power-up Delay

While running on AC power, in order to avoid both motherboards powering up at the same time and drawing larger than normal current, the midplane introduces a delay between the 12.5V power delivered to each of the two motherboards. The delay time can be set between 1 second and 1 minute, with 30 seconds as the default configuration.

The power-up delay behaves as follows:

* When both MB0 and MB1 are installed and AC power is applied, MB0 powers on first, then after 30 seconds (the timer delay), MB1 powers on.
* When both MB0 and MB1 are operating, and you remove and re-insert a motherboard, there is no delay for it to power on again.
* When only MB0 is installed and AC power is applied, there is no delay when it powers on.
* When only MB1 is installed and AC power is applied, there is no delay when it powers on.
* With one motherboard is operating, and another motherboard is inserted, there is no delay when it powers on.
* If no motherboards are installed and AC power is applied, then both MB0 and MB1 are inserted, there is a 30 second timer delay between MB0 and MB1 powering on.

### Hot Swap Controller
In order to have better control of the 12.5VDC power input to each motherboard, the ODM should include two hot swap controllers (one for each motherboard) on the midplane. The hot swap controller provides:

* Inrush current control when the motherboard is inserted and the server is powered on.
* Current limiting protection for short circuit.
* PMBUS interface to enable the PCH to report server input power.

Power System
------------

### Input Voltage

#### Input Voltage Level
The nominal input voltage delivered by the power supply is 12.5VDC. The motherboard can accept and operate normally with an input voltage tolerance range between 10.8V and 13.2V. The motherboard's undervoltage protection level is 10V or less.

#### Capacitive Load
To ensure compatibility with the system power supply, the motherboard cannot have a capacitive load greater than 4000µF. The capacitive load of the motherboard cannot exceed the maximum value of 4000µF under any operating condition listed in [Environmental Requirements][].

#### Input Connector
The power input connector is an FCI 51733-009LF right-angle press-fit header. 

### CPU Voltage Regulation Module (VRM)

#### CPU Maximum Power
The motherboard can handle a processor with a maximum thermal design power (TDP) of 95W.

#### CPU VRM Optimizations
The CPU VRM is optimized to reduce cost and increase the efficiency of the power conversion system. The ODM should use only the minimum number of required phases to support the maximum CPU power defined in 9.2.1. A PSI (power state indicator) allows the shedding of unused phases, letting the VRM operate at its peak efficiency.

#### CPU VRM Efficiency
The minimum efficiency for the CPU VRM is 91% over the 30% to 90% load range and 93% over the 50% to 70% load range, measured from the 12.5V input to the VRM output. 

### Hard Drive Power 
The motherboard supplies power to the system's 14 hard drives. The drives require 12VDC and 5VDC power sources. Power is delivered through a traditional 4-pin floppy disk power connector described in Figure 13.

![][fig13]

[fig13]: ../images/intel_drivePowerConnector.png "Figure 13 Drive Power Connector"

_Figure 13 Drive Power Connector_

Pin | Description |
--- | ----------- |
1   | +5VDC       |
2   | GND         |
3   | GND         |
4   | +12VDC      |
[Figure 13 Drive Power Connector]

For SATA ports inside the miniSAS connector, power will be delivered through a 4-pin (2x2) ATX power connector, which fans out into 4 standard SATA power cables. Pin definition is described in Figure 14.

Pin | Description |
--- | ----------- |
1   | GND         |
2   | GND         |
3   | +5VDC       |
4   | +12VDC      |
[Figure 14 4 Pin ATX Power Connector]

#### Power Requirements
In order for the motherboard to supply 12.5VDC power to the hard drives, the PCB traces must support 14A of continuous power (1A per drive) on the 12.5VDC power rail. In order for the system's 5VDC to supply power to the hard drives, its regulator must support an additional 10.5A (0.75A per drive) of continuous power on the 5VDC power rail. The motherboard must support the inrush current required to start each drive from idle. 

#### Output Protection
The 5V disk output power regulator protects against shorts and overload conditions. 

#### Spin-up Delay
When a hard drive spins up after the system powers on, it draws excessive current on both the 12V and 5V rails. The peak current may reach the 1.5A-2A range in 12V. Each of the 14 hard drives must spin up in sequence. The BIOS implements a 5 second delay between each hard drive spinning up. To enable the hard drive's spin-up delay function, set pin 11 of the SATA hard drive's power cable to NC (No Connection).

### System VRM Efficiency
The ODM supplies high efficiency VRMs for all other voltage regulators over 20W not defined in this specification. All voltage regulation modules over 20W have 91% efficiency over the 30% to 90% load range. 

### Power On
The motherboard powers on upon application of power to the input connector. The use of a power button is not required. The motherboard always resumes operation upon restoration of power in a power failure event.

I/O System
----------

This section describes the motherboard's I/O features.

### PCIe x16 Slot/Riser Card
Both the entry and efficient performance motherboards have one PCIe x16 slot, which holds an x16 PCIe signal from the CPU. The slot location and detailed dimensions are described in the mechanical DXF file. The motherboard also has a PCIe riser card so two full-height PCIe cards can be inserted horizontally and locked in position. Its form factor is 2x4.66 inches.

![][fig15]

[fig15]: ../images/intel_pcieRiser.png "Figure 15 PCIe Riser Card"

_Figure 15 PCIe Riser Card_

The reserved pins on the PCI-E x16 slot on the motherboard are described in Figure 16. 

Pin | Pin Defined       | Description                                           |
--- | ----------------- | ----------------------------------------------------- |
A7  | LAN\_SMB_CLKSMBUS | CLOCK from SMLINK0 of PCH                             |
A8  | LAN\_SMB_DAT      | SMBUS DATA from SMLINK0 of PCH                        |
B12 | LAN\_SMB\_ALERT_N | SMBUS Alert signal to SMLINK0 of PCH                  |
A32 | CLK\_100M_P       | Extra 100MHz clock for second PCIe slot on riser card |
A33 | CLK\_100M_N       |	                                                    |
A50 | SLOT0_CONFIG      | Lower slot on riser card has 1x8 (high), 2 x4 (low)   |
B82 | SLOT1_CONFIG      | Higher slot on riser card has 1x8 (high), 2 x4 (low)  |
B17 | SLOT1\_CPRSNT1_N  | CPRSNT1# for SLOT1 on PCIe riser card                 |
B31 | SLOT1\_CPRSNT2_N  | CPRSNT2# for SLOT1 on PCIe riser card                 |
B48 | SLOT0\_CPRSNT1_N  | CPRSNT1# for SLOT0 on PCIe riser card                 |
B81 | SLOT0\_CPRSNT2_N  | CPRSNT2# for SLOT0 on PCIe riser card                 |
[Figure 16 PCIe x16 Slot Reserved Pin Usage on Motherboard]

The reserved pins on the PCIe x16 slot 0 (low) on the riser card are described in Figure 17.

Pin | Pin Defined       | Description                           |
--- | ----------------- | ------------------------------------- |
A32 | LAN\_SMB_CLK      | SMBUS clock from SMLINK0 of PCH       |
A33 | LAN\_SMB_DAT      | SMBUS data from SMLINK0 of PCH        |
A50 | LAN\_SMB\_ALERT_N | SMBUS alert signal to SMLINK0 of PCH  |
B48 | SLOT0\_CPRSNT1_N  | CPRSNT1# for SLOT0 on PCIe riser card |
B81 | SLOT0\_CPRSNT2_N  | CPRSNT2# for SLOT0 on PCIe riser card |
[Figure 17 PCIe x16 Slot 0 (Low) Reserved Pin Usage on Riser Card]

The reserved pins on the PCIe x16 slot 1 (high) on riser card are described in Figure 18.

Pin | Pin Defined       | Description                           |
--- | ----------------- | ------------------------------------- |
A32 | LAN\_SMB_CLK      | SMBUS clock from SMLINK0 of PCH       |
A33 | LAN\_SMB_DAT      | SMBUS data from SMLINK0 of PCH        |
A50 | LAN\_SMB\_ALERT_N | SMBUS alert signal to SMLINK0 of PCH  |
B17 | SLOT1\_CPRSNT1_N  | CPRSNT1# for SLOT1 on PCIe riser card |
B31 | SLOT1\_CPRSNT2_N  | CPRSNT2# for SLOT1 on PCIe riser card |
[Figure 18 PCIe x16 Slot 1 (High) Reserved Pin Usage on Riser Card]

To support OOB LAN access on the platform controller hub's management engine, a customized PCIe card is needed to use these redefined reserved pins.

### PCIe External Connector
The motherboard has two PCIe x4 external connectors on the efficient performance motherboard and one PCIe x4 external connector on the entry board. These connectors can be used to build a PCIe connection between two systems.

The PCIe x4 connector can be hot inserted and removed. A PCIe re-driver is used for PCIe external links and supports a miniSAS cable up to 2 meters long.

The connector is a miniSAS-4i right-angle connector. External PCI Express target device is TBD. Figure 19 shows the external PCIe pin assignments. The design follows the [PCI Express External Cabling 1.0 Specification](http://www.pcisig.com/members/downloads/specifications/pciexpress/PCI_Express_External_Cabling_Rev1.0_updated.pdf).

Pin Numbers                    | Signals               | Description                                                              |
------------------------------ | --------------------- | ------------------------------------------------------------------------ |
A2/A3, A5/A6, A13/A14, A16/A17 | PER{0..3}{P/N}        | Differential PCI Express receiver lanes                                  |
A1, A4, A7, A12, A15, A18      | GND                   | Ground reference for Differential PCI Express lanes                      |
A8                             | CPRSNT#               | Cable installed/downstream subsystem powered up                          |
A9                             | CPWRON                | Upstream subsystem's power valid notification                            |
A10                            | CWAKE#                | Power management signal for wakeup events (optional)                     |
A11                            | CPERST#               | Cable PERST#                                                             |
B2/B3, B5/B6, B13/B14, B16/B17 | PET{0..3}{P/N}        | Differential PCI Express transmitter lanes                               |
B1, B4, B7, B12, B15, B18      | GND                   | Ground reference for Differential PCI Express lanes                      |
B8                             | SCLK/TX               | SMBUS (PCH SMLINK0) CLOCK (optional UART TX from SIO)                    |
B9                             | SDATA/RX              | SMBUS (PCH SMLINK0) DATA (optional UART RX from SIO)                     |
B10                            | 3.3V/SYS_RST#         | 3.3V standby with 0 ohm in series (Reset signal to trigger system reset) |
B11                            | SB_RTN                | Signal return for single-ended sideband signals                          |
[Figure 19 External PCIe Pin Assignments]


### PCIe Mezzanine Card
The motherboard has one PCIe x8 mezzanine card connector that holds the x8 PCIe signal from cpu0 on both the entry and the efficient performance motherboards. The mezzanine card has two PCIe x4 external connectors (miniSAS) and one mSATA miniPCIe connector.

Pin Name              | Pin | Pin | Pin Name             | Pin Name          | Pin | Pin | Pin Name       |
--------------------- | --- | --- | -------------------- | ----------------- | --- | --- | -------------- | 
P12V                  | 61  | 1   | MEZZ\_PRSNT1\_N      | GND               | 91  | 31  | MEZZ\_RX_DN<0> |
P12V                  | 62  | 2   | P5V\_AUX             | MEZZ\_TX\_DP_C<1> | 92  | 32  | GND            |
P12V                  | 63  | 3   | P5V\_AUX             | MEZZ\_TX\_DN_C<1> | 93  | 33  | GND            |
GND                   | 64  | 4   | P5V\_AUX             | GND               | 94  | 34  | MEZZ\_RX_DP<1> |
GND                   | 65  | 5   | GND                  | GND               | 95  | 35  | MEZZ\_RX_DN<1> |
P3V3\_AUX             | 66  | 6   | GND                  | MEZZ\_TX\_DP_C<2> | 96  | 36  | GND            |
GND                   | 67  | 7   | P3V3\_AUX            | MEZZ\_TX\_DN_C<2> | 97  | 37  | GND            |
GND                   | 68  | 8   | GND                  | GND               | 98  | 38  | MEZZ\_RX_DP<2> |
P3V3                  | 69  | 9   | GND                  | GND               | 99  | 39  | MEZZ\_RX_DN<2> |
P3V3                  | 70  | 10  | P3V3                 | MEZZ\_TX\_DP_C<3> | 100 | 40  | GND            |
P3V3                  | 71  | 11  | P3V3                 | MEZZ\_TX\_DN_C<3> | 101 | 41  | GND            | 
P3V3                  | 72  | 12  | P3V3                 | GND               | 102 | 42  | MEZZ\_RX_DP<3> | 
GND                   | 73  | 13  | P3V3                 | GND               | 103 | 43  | MEZZ\_RX_DN<3> | 
LAN\_3V3STB\_ALERT\_N | 74  | 14  | MEZZ\_CPRSNT1\_N     | MEZZ_TX_DP_C<4>   | 104 | 44  | GND            | 
SMB\_LAN\_3V3STB\_CLK | 75  | 15  | MEZZ\_CPRSNT2\_N     | MEZZ\_TX\_DN_C<4> | 105 | 45  | GND            | 
SMB\_LAN\_3V3STB\_DAT | 76  | 16  | SSD\_PRSNT\_N        | GND               | 106 | 46  | MEZZ\_RX_DP<4> | 
PCIE\_WAKE\_N         | 77  | 17  | RST\_PLT\_MEZZ\_N    | GND               | 107 | 47  | MEZZ\_RX_DN<4> | 
DA\_DSS               | 78  | 18  | MEZZ\_SMCLK          | MEZZ\_TX\_DP_C<5> | 108 | 48  | GND            | 
GND                   | 79  | 19  | MEZZ\_SMDATA         | MEZZ\_TX\_DN_C<5> | 109 | 49  | GND            | 
SATA\_TX+             | 80  | 20  | GND                  | GND               | 110 | 50  | MEZZ\_RX_DP<5> | 
SATA\_TX-             | 81  | 21  | GND                  | GND               | 111 | 51  | MEZZ\_RX_DN<5> | 
GND                   | 82  | 22  | SATA\_RX+            | MEZZ\_TX_DP_C<6>  | 112 | 52  | GND            | 
GND                   | 83  | 23  | SATA\_RX-            | MEZZ\_TX\_DN_C<6> | 113 | 53  | GND            | 
CLK\_100M\_MEZZ2\_DP  | 84  | 24  | GND                  | GND               | 114 | 54  | MEZZ\_RX_DP<6> | 
CLK\_100M\_MEZZ2\_DN  | 85  | 25  | GND                  | GND               | 115 | 55  | MEZZ\_RX_DN<6> | 
GND                   | 86  | 26  | CLK\_100M\_MEZZ1\_DP | MEZZ\_TX\_DP_C<7> | 116 | 56  | GND            | 
GND                   | 87  | 27  | CLK\_100M\_MEZZ1\_DN | MEZZ\_TX\_DN_C<7> | 117 | 57  | GND            | 
MEZZ\_TX\_DP\_C<0>    | 88  | 28  | GND                  | GND               | 118 | 58  | MEZZ\_RX_DP<7> | 
MEZZ\_TX\_DN\_C<0>    | 89  | 29  | GND                  | GND               | 119 | 59  | MEZZ\_RX_DN<7> | 
GND                   | 90  | 30  | MEZZ\_RX\_DP<0>      | MEZZ\_PRSNT2_N    | 120 | 60  | GND            | 
[Figure 20 PCIe Mezzanine Card Connector Pin Definition]

### DIMM Connector
The motherboard uses a 30u" gold contact for the DDR3 DIMM connector.

### Network
The motherboard has an Intel® 82574L Ethernet interface to the front RJ45 connector. It has a PCIe x1 lane routed to the PCH.

The motherboard has an Intel® I350 dual port network chip. It has a single Ethernet interface to the front RJ45 connector. It has PCIe x2 lanes routed to the PCH on entry board, while it has PCIe x4 lanes routed to the PCH on efficient performance board. 

The BIOS supports PXE boot on all RJ45 ports on the motherboard.

Each RJ45 connector has two built-in LEDs. While facing the RJ45 connector, the left LED is green single color; solid on means the link is active and blinking means activity. The right LED is green/yellow dual color; green means 100M link speed while yellow means 1000M link speed.

#### Reboot on WOL in S0 State
Reboot on WOL (ROW) is a feature that repurposes the traditional Wake on LAN (WOL) signal to reboot the motherboard. While the system is in S0 state (running), when a WOL packet is received by the NIC, the wakeup signal generated by the NIC causes a hardware reboot of the motherboard. This is accomplished by tying the WOL interrupt pin of the NIC to the system's master reboot signal. ROW does not require the power supply to cycle its output. 

There is an optional ROW connection for the WAKE# signal from PCIe slot and external PCIe connector, which gives optional ROW support for add-in cards and external PCIe devices. 

ROW is enabled by the NIC EEPROM, so the appropriate NIC EEPROM for the 82574 and I350 interface must be used. The motherboard also supports ROW on both the PCIe LAN card and the mezzanine LAN card, which includes hardware circuit support and NIC EEPROM enabling. 

### USB Interfaces
The motherboard has two external USB ports located in the front of the motherboard. The BIOS supports the following USB devices: 

* Keyboard and mouse
* USB flash drive (bootable)
* USB hard drive (bootable)
* USB optical drive (bootable)

### SATA
The motherboard has a next generation Intel® platform controller hub on board and supports the SATA ports and the miniSAS connectors. The HDDs attached to all the SATA connectors follow the spin-up delay described in [Spin-up Delay][].

### Debug Header
The motherboard includes a debug header on the front of the motherboard to display POST codes (see [Post Codes][]). The debug header supports hot plugging. 

The debug card has two 7-segment LED displays, one RS-232 serial connector, and one reset switch. The RS-232 serial port provides console redirection. The two 7-segment LED displays show BIOS POST code and DIMM error information. The reset switch triggers a system reset when pressed.

The connector for the debug header is a 14-pin, shrouded, vertical, 2mm pitch connector. Figure 21 is an illustration of the headers. The debug card has a key to match with the notch to avoid pin shift when plugging it in.

![][fig21]

[fig21]: ../images/intel_debugHeader.png "Figure 21 Debug Header"

_Figure 21 Debug Header_

Pin (CKT) | Function                                     |
--------- | -------------------------------------------- |
1         | Low HEX character [0] least significant bit  |
2         | Low HEX character [1]                        |
3         | Low HEX character [2]                        |
4         | Low HEX character [3] most significant bit   |
5         | High HEX character [0] least significant bit |
6         | High HEX character [1]                       |
7         | High HEX character [2]                       |
8         | High HEX character [3] most significant bit  |
9         | Serial transmit (motherboard transmit)       |
10        | Serial receive (motherboard receive)         |
11        | System reset                                 |
12        | Serial console select (1=SOL; 0=local)       |
13        | GND                                          |
14        | VCC (+5VDC)                                  |
[Figure 22 Debug Header Pin Definitions]

#### Post Codes
POST codes are sent to the debug header in hexadecimal format via two hex codes. The hex codes can be driven by either the legacy parallel port (port 80) on the SIO, or 8 GPIO pins. 

During the boot sequence, the BIOS initializes and tests each DIMM. If a module fails initialization or does not pass the BIOS test, one of the following POST codes will flash on the debug card to indicate which DIMM has failed. The first hex character indicates which CPU interfaces the DIMM module; the second hex character indicates the number of the DIMM module. The BIOS flashes the corresponding hex code indefinitely to allow time for a technician to service the system. The DIMM number count starts from the DIMM furthest from the CPU.

#### Serial Console
The output stage of the system's serial console is contained on the debug card. The TX and RX signals from the SIO are sent to the debug header at the chip's logic levels (+3.3V). The debug card contains the RS-232 level shifter and the RS-232 D-9 connector.
By default, the host does console redirection through serial over LAN (SOL). When the debug card is connected, debug card pin 12 is used to select console redirection between SOL and the local serial port on the card, as described in Figure 22.

### Switches and LEDs
The motherboard includes a power switch, reset switch, power LED, HDD activity LED, and beep error LED.

#### Switches
The front edge of the PCB has right angle pushbutton switches. One switch is used as the system's power button the second switch is used at the system's reset button. 

**Note:** If the ODM chooses to use smaller tactile switches, the push button actuator must be a minimum 2.5mm diameter and protrude at least 1.5mm from the switch's enclosure.

If the power switch is depressed for less than four seconds, a power management event is issued, indicating that the power switch has been triggered. If the power switch is depressed for more than four seconds, the motherboard performs a hard power off.

If the reset switch is depressed for any length of time, the motherboard performs a hard reset and begins executing the BIOS initialization code.

Each switch is identified by a label on the motherboard's silkscreen. The power button is labeled PWR and the reset button is labeled RST.

#### LEDs
The motherboard has 3 LEDs on the front edge. Figure 23 identifies each LED's color, function, and silkscreen label. The label describes the functionality of each LED. 

LED Color | Function | Silkscreen Label |
--------- | -------- | ---------------- |
Blue      | Power LED. This LED has the same functionality of a traditional PC power LED. It illuminates only if the motherboard is in the powered on state. | PWR |
Green     | Hard drive activity. This LED illuminates when there is activity on the motherboard's SATA hard drive interfaces. | HDD |
Yellow    | This LED replaces the functionality of the PC speaker. The motherboard causes the LED to illuminate for the same duration and sequence as the PC speaker would normally beep. The LED allows for easier diagnosis in a noisy data center environment. | BEEP |
[Figure 23 LED Functionality]

The beep error LED patterns are described in Figure 24.

Error Description                    | LED Patterns                                                                | | | | | | |
------------------------------------ | ----------------------------------------------------------------------------------------| 
Memory refresh timer error           | On (2s)    | Off (0.25s) | On (2s)    | Off (0.25s) | On (2s)    | Off (3s) | …(repeat) |
Base memory read/write test error    | On (2s)    | Off (0.25s) | On (2s)    | Off (0.25s) | On (0.25s) | Off (3s) | …(repeat) |
Keyboard controller BAT test error   | On (0.25s) | Off (0.25s) | On (0.25s) | Off (0.25s) | On (2s)    |          |           | 
General exception error              | On (2s)    | Off (0.25s) | On (0.25s) | Off (0.25s) | On (0.25s) | Off (3s) | …(repeat) | 
Display memory error                 | On (0.25s) | Off (0.25s) | On (0.25s) | Off (0.25s) | On (0.25s) |          |           | 
[Figure 24 Beep Error LED Patterns]

Mechanical
----------

Figure 25 shows the basic view of the Open Compute Project server chassis. Refer to mechanical step file provided for detailed information.

![][fig25]

[fig25]: ../images/ocp_chassis.png "Figure 25 Open Compute Project Server Chassis for Intel Motherboards"

_Figure 25 Open Compute Project Server Chassis for Intel Motherboards_

### Fixed Locations
Refer to the mechanical DXF file for fixed locations of the mounting hole, PCIe x16 slot, and power connector.

### PCB Thickness
To ensure proper alignment of the FCI power connector and mounting within the mechanical enclosure, the boards should follow the PCB stackups described in sections <a href="#ENPCB">4.5</a> and <a href="#EPPCB">5.5</a> respectively and have 85mil (2.16mm) thickness. The mid-plane PCB thickness is also 85mil (2.16mm). The mezzanine card PCB thickness is 62mil (≈1.6mm).

### Heat Sinks
The motherboard supports customized CPU heat sinks that are mounted according to the Intel specifications. The mounting device employs a backplate and receptacles for screw-down type heat sinks. The ODM must provide all keep out zones defined by Intel to ensure the heat sinks mount correctly on the board.

### Silkscreen
The silkscreen is white in color and includes labels for these components: 

* cpu0/cpu1
* eth0/eth1
* DIMM slot numbering, as described in [Post Codes]
* [LEDs]
* [Switches]

### DIMM Connector Color

Colored DIMM connectors indicate the first DIMM of each memory channel, whereas the remaining DIMM connectors on the same memory channel are a different color. The first DIMM on each channel is defined as the DIMM placed physically furthest from its associated CPU. This DIMM connector must be populated first when memory is only partially populated.

Environmental Requirements
--------------------------

The motherboard meets the following environmental requirements:

* Gaseous Contamination: Severity Level G1 per ANSI/ISA 71.04-1985
* Ambient operating temperature range: -5°C to +45°C
* Operating and storage relative humidity: 10% to 90% (non-condensing)
* Storage temperature range: -40°C to +70°C
* Transportation temperature range: -55°C to +85°C (short-term storage)

The full OCP system also meets these requirements. In addition, the full system has an operating altitude with no de-ratings of 1000m (3300 feet).
 
### Vibration and Shock
The motherboard meets shock and vibration requirements according to the following IEC specifications: IEC78-2-(\*) and IEC721-3-(*) Standard & Levels. The testing requirements are listed in Figure 26. 

&nbsp;    | Operating | Non-Operating |
|-------- | --------- | ------------- | 
Vibration | 0.5g acceleration, 1.5mm amplitude, 5 to 500 Hz, 10 sweeps at 1 octave/minute for each of the three axes (one sweep is 5 to 500 to 5 Hz) | 1g acceleration, 3mm amplitude, 5 to 500 Hz, 10 sweeps at 1 octave/minute for each of the three axes (one sweep is 5 to 500 to 5 Hz)
Shock     | 6g, half-sine 11mS, 5 shocks for each of the three axes | 12g, half-sine 11mS, 10 shocks for each of the three axes | 
[Figure 26 Vibration and Shock Requirements]

Prescribed Materials
--------------------

### Disallowed Components
The following components are not used in the design of the motherboard:

* Components disallowed by the European Union's Restriction of Hazardous Substances Directive (RoHS 6)
* Trimmers and/or potentiometers
* Dip switches

### Capacitors and Inductors
The following limitations apply to the use of capacitors:

* Only aluminum organic polymer capacitors made by high quality manufacturers are used; they must be rated 105C
* All capacitors have a predicted life of at least 50,000 hours at 45C inlet air temperature, under worst conditions
* Tantalum capacitors are forbidden
* SMT ceramic capacitors with case size > 1206 are forbidden (size 1206 are still allowed when installed far from the PCB edge and with a correct orientation that minimizes risks of cracks) 
* Ceramic material for SMT capacitors must be X7R or better material (COG or NP0 type should be used in critical portions of the design)
Only SMT inductors may be used. The use of through hole inductors is disallowed.

### Component De-rating
For inductors, capacitors, and FETs, de-rating analysis should be based on at least 20% de-rating.


