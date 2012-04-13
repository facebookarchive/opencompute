latex input:        mmd-article-header
Title:              Open Compute Project AMD Motherboard Hardware v2.0
Base Header Level:  2  
CSS:                /base.css
LaTeX Mode:         memoir  
latex input:        mmd-article-begin-doc
latex footer:       mmd-memoir-footer

![][header1]

[header1]: ../../alpha/images/OCPlogo_vert.png

Open Compute Project AMD Motherboard Hardware v2.0
==========================================================

Author: Harry Li, Engineer

Author: Amir Michael, Engineer

<!-- \pagebreak -->
<!-- \pagestyle{fancy} -->

Scope
-----
This document defines the technical specifications for the AMD motherboard used in Open Compute servers.

Contents
--------

<!--  \tableofcontents -->

Overview
--------
When data center design and hardware design move in concert, they can improve efficiency and reduce power consumption. To this end, the Open Compute Project is a set of technologies that reduces energy consumption and cost, increases reliability and choice in the marketplace, and simplifies operations and maintenance. One key objective is openness—the project is starting with the opening of the specifications and mechanical designs for the major components of a data center, and the efficiency results achieved at facilities using Open Compute technologies.

One component of this project is a custom motherboard. This document describes the Open Compute Project AMD motherboard, a dual AMD G34 socket motherboard with 16 DIMM slots. The motherboard is power-optimized and barebones, designed to provide the lowest capital and operating costs. Many features found in traditional motherboards have been removed from the design.

### License
As of June 23, 2011, the following persons or entities have made this Specification available under the Open Web Foundation Final Specification Agreement (OWFa 1.0), which is available at [www.openwebfoundation.org/legal/the-owf-1-0-agreements/owfa-1-0](http://www.openwebfoundation.org/legal/the-owf-1-0-agreements/owfa-1-0): 

Facebook, Inc.

You can review the signed copies of the Open Web Foundation Agreement Version 1.0 for this Specification at http://opencompute.org/licensing/, which may also include additional parties to those listed above. 
Your use of this Specification may be subject to other third party rights. THIS SPECIFICATION IS PROVIDED "AS IS." The contributors expressly disclaim any warranties (express, implied, or otherwise), including implied warranties of merchantability, non-infringement, fitness for a particular purpose, or title, related to the Specification. The entire risk as to implementing or otherwise using the Specification is assumed by the Specification implementer and user. IN NO EVENT WILL ANY PARTY BE LIABLE TO ANY OTHER PARTY FOR LOST PROFITS OR ANY FORM OF INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES OF ANY CHARACTER FROM ANY CAUSES OF ACTION OF ANY KIND WITH RESPECT TO THIS SPECIFICATION OR ITS GOVERNING AGREEMENT, WHETHER BASED ON BREACH OF CONTRACT, TORT (INCLUDING NEGLIGENCE), OR OTHERWISE, AND WHETHER OR NOT THE OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

### CAD Models
The following CAD files are incorporated by reference as if fully set forth in this specification:

* TBD

Motherboard Features
--------------------

### Block Diagram

Figure 1 illustrates the functional block diagram of the motherboard. 

![][fig1]

[fig1]: ../images/amd_block.png "Figure 1 Functional Block Diagram"

_Figure 1  Functional Block Diagram_

### Placement and Form Factor
The motherboard's form factor is 6.6x20 inches. Figure 2 illustrates board placement. The placement shows the relative positions of key components, while exact dimension and position information is available in the DXF file and mechanical information is in the 3D CAD model. The ODM should strictly follow the form factor, PCI-E slot position, front IO port positions, PCI-E mezzanine card connector position, power connector, and mounting holes, while other components can be shifted based on layout routing as long as relative position is maintained. As shown in Figure 17, one Open Compute chassis accommodates two motherboards. In order to remove and install one board without affecting the other board, the following internal connectors are placed as close as possible to the front of the board in order to have easy frontal access:

* One SATA signal connector and one SATA power connector.
* Debug card header.

![][fig2]

[fig2]: ../images/amd_placement.png "Figure 2 AMD Motherboard Component Placement"

_Figure 2 AMD Motherboard Component Placement_

### CPU and Memory
The motherboard supports two AMD G34 Magny Cours or Interlagos CPUs with a TDP (thermal design power) of 115W. The motherboard supports these features:

* HT3 16x16 link HyperTransport™ links between CPUs with cHT3 target of up to 6.4 GT/s (with probe filter)
* 1 ncHT3 16x16 link to SR56X0 chipset with target speed of up to 5.2 GT/s
* Single Processor Mode 
* DDR3 direct attached memory support on cpu0 and cpu1 with:
    * 4 channels DDR3 registered memory interface on each CPU
    * 2 DDR3 slots per channel per processor (total of 16 DIMMs on the motherboard)
    * RDIMM/LV-RDIMM (1.35V/1.25V), LRDIMM, and UDIMM/LV-UDIMM (1.35V/1.25V) 
    * SR, DR, and QR DIMMs 
    * DDR3 speeds of 800/1066/1333/1600
    * Up to maximum 512GB memory with 32GB RDIMMs

### Northbridge PCI-E Usage

The motherboard supports PCI-E lane configuration as illustrated in Figure 3. Depending upon the chipset, different PCI-E interfaces are supported:

* With the SR5650 chipset, the board supports one x16 PCI-E riser card. 
* With the SR5670 chipset, the board supports one x16 PCI-E riser card and one x4 PCI-E mezzanine card. 
* With the SR5690 chipset, the board supports one x16 PCI-E riser card, one x4 PCI-E mezzanine card, and one x4 PCI-E external connector.

Device                                | Number of PCI-E Lanes                         | 
------------------------------------- | --------------------------------------------- | 
x16 PCI-E slot                        | 16 (from GPP1)                                |
x4 PCI-E mezzanine card               | 4 (from GPP2[3:0], requires SR5670 or SR5690) |
x4 PCI-E external connector (miniSAS) | 4 (from GPP3 [9:6], requires SR5690)          |
Intel 82576 NIC                       | 4 (from GPP3 [3:0])                           |
Total number of lanes                 | 28                                            |
[Figure 3 PCI-E Lane Usage]

### Southbridge/Peripheral Bus Controller
The motherboard uses the AMD SP5100 Southbridge chipset, which supports the following features:

* 2 USB 2.0 ports (on the front panel)
* 6 SATAII ports
* SPI interface
* SMBUS interface (master and slave)

BIOS
----

The ODM is responsible for supplying and customizing a BIOS for the motherboard. The specific BIOS requirements are outlined in this section.

### BIOS Chip

The BIOS uses the SP5100's SPI interface. The ODM is responsible for selecting a specific BIOS chip that meets the required functionality. 

### BIOS Socket

A socket on the motherboard holds the BIOS chip, which allows for manual replacement of the BIOS chip. The BIOS socket is easily accessible; other components on the motherboard do not interfere with the insertion or removal of the BIOS chip.

### BIOS Source Code
The BIOS source code comes from AMI. The ODM is responsible for maintaining the BIOS source code to make sure it has latest code release from AMI and AMD.

### BIOS Configuration and Features
The BIOS is tuned to minimize system power consumption. It has the following features:

* Unused devices disabled, including PCI-E lanes, PCI, USB ports, and SATA/SAS ports
* Tuning CPU/chipset settings to reach minimized power consumption and best performance
* SPECpower is used as guidance for ODM to validate BIOS tuning results

### BIOS Setup Menu
The ODM must provide a BIOS specification, which includes the complete BIOS, setup menu, and default settings. The setup menu allows its options to be configured before the operating system loads. The configuration options available through the boot menu include the following:

* Settings to adjust memory speed, HT link speed, HT link width, and CPU Cx/Px power state.
* Setting for power feature after AC failure; default is set to keep last state.
* Setting for console redirection. Selectable options to support select console redirection from local COM port or the BMC's virtual UART for SOL.
* Hardware health monitoring display.
* Setting for watchdog timer; default is enabled and timeout value is 15 minutes.
* Event log viewing and clearing.
* Setting for ECC error threshold, available settings are 1, 4, 10, and 1000.
* If a CMOS checksum error happens (for example, caused by a BIOS update), the BIOS loads the system default automatically after showing a text message in the console for 5 seconds and rebooting the system to apply the update without user input.
* Setting to disable all "wait for keyboard input to continue" features.

### Console Redirect

The BIOS detects the presence of a video card in the x16 PCI-E slot. If a video card is present, the BIOS directs its output to the video card. If no video card is present, the BIOS directs its output to the board-mounted RS-232 console output.

### PXE Boot

The BIOS supports Intel PXE boot. When PXE booting, the system first attempts to PXE boot from the first Ethernet interface (eth0). If a PXE boot on the first Ethernet interface fails, the BIOS attempts to PXE boot from the second Ethernet interface (eth1). 

### Other Boot Options

The BIOS also supports booting from SATA and USB interfaces. The BIOS provides the capability to select boot options.

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

Additionally, the update tool(s) should have the following capabilities:

* Update from the operating system over the LAN – the OS standard is CentOS v5.2
* Can complete update with a single reboot (no PXE boot, no multiple reboots) 
* BIOS update or BIOS setup option change take no more than 5 minutes to complete
* No user interaction (like prompts)
* Can be scripted and propagated to multiple machines

### Event Log
The BIOS logs system events through the baseboard management controller (BMC).

#### Logged Errors

* **CPU/memory errors:** Both correctable ECC and uncorrectable ECC errors should be logged into event log. Error categories include DRAM, HyperTransport™ Link, and L3 Cache.
* **HyperTransport™ errors:** Any errors that have a status register should be logged into the event log. Fatal or non-fatal classification follows the chipset vendor's recommendation.
* **Internal parity errors:** All errors that have status register should be logged into the event log. Fatal, non-fatal, or correctable classification follows the chipset vendor's recommendation.
* **PCI-E errors:** All errors that have status register should be logged into Event Log, including root complex, endpoint device and any switch upstream/downstream ports if available. Link disable on errors should also be logged. Fatal, non-fatal, or correctable classification follows the chipset vendor's recommendation.
* **POST errors:** All POST errors detected by the BIOS during POST should be logged into the event log.
* **Power errors:** Two power errors should get logged: 
    * When a 12.5VDC input power failure causes all power rails on the motherboard to lose power, including standby power.
    * When an unexpected system shutdown occurs during system S0/S1 while 12.5VDC input is still valid.
* **MHOT and PROCHOT errors:** MEMHOT events should be logged with event source information indicating whether the event was triggered by a DIMM or a DIMM's voltage regulator. PROCHOT events should be logged with event source information indicating whether the event was triggered by a CPU or the CPU's voltage regulator.

#### Error Threshold Settings
An error threshold setting must be enabled for both correctable and uncorrectable errors. Once the programmed threshold is reached, an event should be triggered and logged.

* **Memory Correctable ECC:** The threshold value is 1000. When the threshold is reached, the BIOS should log the event including DIMM location information and output DIMM location code through the Facebook debug card.
* **HyperTransport™ errors:** Follow the chipset vendor's suggestion.
* **PCI-E errors:** Follow the chipset vendor's suggestion.

Hardware Monitoring and Fan Speed Control
-----------------------------------------

The ODM needs to provide a system access interface and application to retrieve hardware monitoring sensor readings, including at minimum, lm_sensors, a Linux application for the CentOS operating system and its driver. The sensors to be read include voltage, temperature, and fan speed.

The <a href="#bmc">BMC</a> can be used to monitor hardware and control fan speed. 

### Thermal Sensors

The motherboard has five thermal sensors:

* Two to monitor temperatures for CPU0 and CPU1, retrieved through the CPU's temperature sensor interface (TSI)
* Northbridge temperature
* Inlet temperature, retrieved through the thermistor, and located in the front of the motherboard
* Outlet temperature, retrieved through the thermistor, and located in the rear of the motherboard
The sensors should make sure that no CPU throttling is triggered due to thermal issues, under the following environmental conditions:
* Inlet temperature lower than or equal to 30°C, and 0 inch H2O data center pressure with all fans in each thermal zone running functionally
* Inlet temperature lower than or equal to 30°C, and 0.01 inch H2O pressure with one fan (or one rotor) in each thermal zone failing

### Fan Connection

Each motherboard has fan tachometers and PWM connections to two system fans through the midplane.

<a name="bmc"></a>
Baseboard Management Controller
-------------------------------

The BMC performs various functions for the motherboard, which are described in this section.

### Fan Speed Control

The BMC provides a fan control algorithm that ensures adequate cooling of the system in the chassis. The BMC can update the FSC configuration both locally (through the CentOS host OS) and remotely (through OOB); these updates take effect immediately without rebooting.

### Power Monitoring

The BMC supports platform power monitoring for the whole server. This is accessible both through in-band, and out-of-band by LAN or IPMB (Intelligent Platform Management Bus). 

### Serial-Over-LAN

The BMC supports serial-over-LAN (SOL) through the single shared network interface available on the motherboard. 

### Remote Power Control

The BMC supports remote system power on/off and reboot through LAN or IPMB.

### System Event Log

The BMC supports a system event log. See [Event Log] for more information.

### Firmware Update

The ODM must provide tool(s) to implement remote BIOS firmware update, which does not require any physical input at the system. Remote update means either through out-of-Band by the BMC or through logging into the local OS (CentOS 5.2) over the network. 
 
Midplane
--------

The midplane is a PCB board that functions as a bridge between the system fans, power supply (PSU), and both motherboards. Its form factor is 2x13.4 inches. 

### PSU Connector

The midplane has one FCI 51939-582 male right angle header, which is mated directly with the PSU for 12.5VDC input. Figure 4 shows the pin definition and direction based on the PSU.

Pin #  | Signals       | Direction | Description                | Usage                   |
------ | ------------- | --------- | -------------------------- | ----------------------- |
P1, P2 | P12V          | Power     | 12.5VDC                    | 12.5VDC                 |
P3, P4 | GND           | Power     | Ground                     | Ground                  |
A1     | AUX\_RTN_GND  |           | Signal return              | NC                      |
A2     | BACKUP_N      | Output    | PSU backup mode indication | NC                      |
B1     | SHARE\_SEL_1  | Input     | PSU mode selection         | NC                      |
B2     | SHARE\_SEL_2  | Input     | PSU mode selection         | NC                      | 
C1     | GREEN\_LED_N  | Output    | Low active                 | Connect to bi-color LED | 
C2     | YELLOW\_LED_N | Output    | Low active                 | Connect to bi-color LED | 
D1     | RED\_LED_N    | Output    | Low active                 | Connect to LED          | 
D2     | P5V_AUX       | Power     | 5V for LED, 50mA limited   | LED power               | 
[Figure 4 Midplane to PSU Connector Pin Definition]

For the PSU LED, the midplane provides a 4-pin vertically shrouded 2.54mm pitch header with latch. This allows an LED cable to extend the PSU LED to the chassis front. The PSU connector pins C1 and C2 connect to one bi-color (green/yellow) LED with a common anode. Pin D1 is connected to one red LED. Pin D2 is 5V and used for an LED anode. Both are 3mm LEDs. A current limit resistor is required for each LED signal.

Pin | Description   |
--- | ------------- |
1   | GREEN\_LED_N  |
2   | YELLOW\_LED_N |
3   | RED\_LED_N    |
4   | P5V_AUX       |
[Figure 5 PSU LED Header Pin Definition]

When the PSU's red LED blinks (at 1Hz, 50% duty-cycle), it indicates a PSU fan failure. 

### Fan Connectors

The midplane has connectors for the four system fans. The connector signals comply both mechanically and electrically with the specifications defined in the 4-Wire Pulse Width Modulation (PWM) Controlled Fans Specification Revision 1.3 September 2005 published by Intel Corporation. Each fan is driven by dedicated PWM signal. Figure 6 defines the proper pin-out of the connector.

Pin | Description |
--- | ----------- |
1   | GND         |
2   | 12VDC       |
3   | Sense       | 
4   | Control     | 
[Figure 6 Fan Header Pin-out]

A fan tachometer signal from each fan is routed to acquire fan speed. The midplane directly delivers 12.5V power to the fan connector. If one motherboard is not powered on, then its two corresponding fans are turned off to save power.

### Motherboard Connectors

The midplane has two FCI 51770-044 female right-angle power/signal connectors (2P+16S+2P: 4 power blades and 16 signals). The motherboard with mated FCI 51730-162 male right angle header slides in and mates with one of the FCI headers on the midplane. Figure 7 shows the pin definition of the 2P+16S+2P connector; the direction is based on the midplane.

Pin #          | Signal         | Direction    | Description                                             | 
-------------- | -------------- | ------------ | ------------------------------------------------------- |
P1, P2         | P12V           | Power        | 12.5VDC                                                 | 
P3, P4         | GND            | Power        | Ground                                                  | 
A1             | SMB\_ALT_N     | Output       | SMBUS alert signal from hot-swap controller             |
A2             | TACH1A         | Output       | Reserved for extra fan tachometer on FAN1               |
A3             | TACH2A         | Output       | Reserved for extra fan tachometer on FAN2               |
A4             | RSVD           |              | Reserved for future                                     |
B1             | SCLK           | Bi-direction | SMBUS CLOCK                                             |
B2             | SDATA          | Bi-direction | SMBUS DATA                                              |
B3             | MB_ON          | Input        | Indicates that motherboard starts powered on            |
B4             | PSU_PG         | Output       | High active, indicates that PSU 12.5VDC output is ready |
C1             | FAN1_TACH      | Output       | System fan #1 tachometer                                |
C2             | FAN1_PWM       | Input        | System fan #1 PWM                                       |
C3             | FAN2_TACH      | Output       | System fan #2 tachometer                                |
C4             | FAN2_PWM       | Input        | System fan #2 PWM                                       |
D1 (short pin) | MATED_N        | Input        | Low active, indicates motherboard is fully mated        |
D2             | MATED\_GND_RTN |              | Connected to GND in midplane                            |
D3             | MB_ID          | Output       | Motherboard ID = 0 (left), 1 (right)                    |
D4             | FAN\_FAIL_N    | Output       | PSU fan failure detected                                |
[Figure 7 Midplane to Motherboard Connector Pin Definition]

### HDD Power Connector

The midplane has two HDD 4-pin power connectors, allowing for the routing of two HDD power cables directly from the midplane to the two hard drives.

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
* Current limiting protection for short circuits.
* PMBUS interface to enable the BMC to report server input power.

Power System
------------

### Input Voltage

#### Input Voltage Level
The nominal input voltage delivered by the power supply is 12.5VDC. The motherboard can accept and operate normally at an input voltage tolerance range between 10.8V and 13.2V. The motherboard's under-voltage protection level is 10V or below.

#### Capacitive Load
To ensure compatibility with the system power supply, the motherboard cannot have a capacitive load greater than 4000µF. The capacitive load of the motherboard should not exceed the maximum value of 4000µF under any operating condition listed in [Environmental Requirements].

#### Input Connector
The power input connector is an FCI 51730-162 male right-angle header. CPU Voltage Regulation Module (VRM)

#### CPU Maximum Power
The motherboard can handle a processor with a maximum thermal design power (TDP) of 115W.

#### CPU VRM Optimizations
The CPU VRM is optimized to reduce cost and increase the efficiency of the power conversion system. The ODM should only use the minimum number of required phases to support the maximum CPU power defined in [CPU and Memory]. A PSI (power state indicator) allows the shedding of unused phases, letting the VRM operate at its peak efficiency.

#### CPU VRM Efficiency
The minimum efficiency for the CPU VRM is 91% over the 30% to 90% load range and 93% over the 50% to 70% load range for TDP 115W CPU, measured from the 12.5V input to the VRM output. 

### Hard Drive Power 
The motherboard supplies power to the system's six hard drives. The drives require 12VDC and 5VDC power sources. For one individual SATA port, power is delivered through a traditional 4-pin floppy disk power connector described in Figure 8.

![][fig8]

[fig8]: ../images/amd_hardDrivePower.png "Figure 8 Drive Power Connector"

Pin | Description |
--- | ----------- |
1   | +5VDC       |
2   | GND         |
3   | GND         |
4   | +12VDC      |
[Figure 8 Drive Power Connector]

For the other five SATA ports, power is delivered through a 4-pin (2x2) ATX power connector, which fans out to five standard SATA power cables. Pin definition is described in Figure 9.

Pin	Description
1	GND
2	GND
3	+5VDC
4	+12VDC
[Figure 9 4 Pin ATX Power Connector]

#### Power Requirements
The motherboard must deliver enough current on both the 12.5VDC and 5VDC rails to power all 6 hard drives this platform supports. The PCB traces must support 1A of continuous power per HDD (6A total) on the 12.5VDC power rail, and 0.75A of continuous power per HDD (4.5A total) on the 5VDC power rail. It must support the inrush current required by each drive. 

#### Output Protection
The 5V disk output power regulator protects against shorts and overload conditions. 

#### Spin-up Delay
When the hard drive spins up after the system powers on, it draws excessive current on both 12V and 5V. The peak current may reach 1.5A - 2A range in 12V. Each of the system's six hard drives must spin up in sequence. 
As an option, the BIOS can implement a 5 second delay between each hard drive spinning up. To enable the hard drive's spin-up delay function, set pin 11 of the SATA hard drive's power cable to NC (No Connection).

### System VRM Efficiency
The ODM must supply high efficiency VRMs for all other voltage regulators over 20W not defined in this specification. All voltage regulation modules over 20W must have 91% efficiency over the 30% to 90% load range. 

### Power State
The motherboard returns to the previous power state upon application of power to the input connector. The use of a power button is not required. The motherboard always resumes operation upon restoration of power in a power failure event if the previous power state is power on.

I/O System
----------

This section describes the motherboard's I/O features.

### PCI-E x16 Slot/Riser Card
The motherboard has one PCI-E x16 slot, which holds an x16 PCI-E Gen 2 signal from Northbridge (SR56x0). The slot location is described in the mechanical DXF file. The motherboard also has a PCI-E riser card so two standard profile PCI-E cards (4.376" maximum height and 6.6" maximum length, based on the PCI Express Card Electromechanical Specification Rev 2.0) can be inserted horizontally and locked in position.

### PCI-E Mezzanine Card
The motherboard has one PCI-E x4 mezzanine card connector that holds the x4 PCI-E Gen 2 signal from Northbridge (SR5670). 

### PCI-E External Connector
The motherboard has one PCI-E x4 (miniSAS) external connector on board. This PCI-E x4 connector can be used to build a PCI-E connection between two systems.

The x4 connector can be hot inserted and removed. A PCI-E re-driver is used for PCI-E external links and supports a miniSAS cable up to 2 meters long.

The connector is a miniSAS-4i right-angle connector. The external PCI Express target device is TBD. Figure 10 shows the external PCI-E pin assignments. The design follows the [PCI Express External Cabling 1.0 Specification](http://www.pcisig.com/members/downloads/specifications/pciexpress/PCI_Express_External_Cabling_Rev1.0_updated.pdf).

Pin Numbers                    | Signals        | Description                                                              | 
------------------------------ | -------------- | ------------------------------------------------------------------------ | 
A2/A3, A5/A6, A13/A14, A16/A17 | PER{0..3}{P/N} | Differential PCI Express receiver lanes                                  | 
A1, A4, A7, A12, A15, A18      | GND            | Ground reference for Differential PCI Express lanes                      | 
A8                             | CPRSNT#        | Cable installed/downstream subsystem powered up                          | 
A9                             | CPWRON         | Upstream subsystem's power valid notification                            | 
A10                            | CWAKE#         | Power management signal for wakeup events (optional)                     | 
A11                            | CPERST#        | Cable PERST#                                                             | 
B2/B3, B5/B6, B13/B14, B16/B17 | PET{0..3}{P/N} | Differential PCI Express transmitter lanes                               | 
B1, B4, B7, B12, B15, B18      | GND            | Ground reference for Differential PCI Express lanes                      | 
B8                             | SCLK/TX        | SMBUS (BMC) CLOCK (optional UART TX from SIO)                            | 
B9                             | SDATA/RX       | SMBUS (BMC) DATA (optional UART RX from SIO)                             | 
B10                            | 3.3V/SYS_RST#  | 3.3V standby with 0 ohm in series (reset signal to trigger system reset) | 
B11                            | SB_RTN         | Signal return for single-ended sideband signals                          | 
[Figure 10 External PCI-E Pin Assignments]

### DIMM Connector
The motherboard uses a 30u" gold contact for the DDR3 DIMM through-hole connector.

### Network
The motherboard has one 82576 LAN chip on board to support the RJ45 connector in the front. The BIOS supports PXE boot on the RJ45 port.
Each RJ45 connector has two built-in LEDs. While facing the RJ45 connector, the left LED is green single color; solid on means the link is active and blinking means activity. The right LED is green/yellow dual color; green means 100M link speed while yellow means 1000M link speed.

#### Reboot on WOL in S0 State
Reboot on WOL (ROW) is a feature that repurposes the traditional Wake on LAN (WOL) signal to reboot the motherboard. While the system is in S0 state (running), when a WOL packet is received by the NIC, the wakeup signal generated by the NIC causes a hardware reboot of the motherboard. This is accomplished by tying the WOL interrupt pin of the NIC to the system's master reboot signal. ROW does not require the power supply to cycle its output. 

There is an optional ROW connection for the WAKE# signal from PCI-E slot and external PCI-E connector, which gives optional ROW support for add-in cards and external PCI-E devices. 

ROW is enabled by the NIC EEPROM, so the appropriate NIC EEPROM for the 82576 chip must be used. The motherboard also supports ROW on both the PCI-E LAN card and the mezzanine LAN card, which includes hardware circuit support and NIC EEPROM enabling. 

#### Out of Band Network Access
The motherboard supports out of Band (OOB) network access to the BMC through network interfaces on the 82576 chip. This includes all remote access features described in this specification. 

### USB Interfaces
The motherboard has two external USB ports located in the front of the motherboard. The BIOS supports the following USB devices: 

* Keyboard and mouse
* USB flash drive (bootable)
* USB hard drive (bootable)
* USB optical drive (bootable)

### SATA
The motherboard has SP5100 interfaces on board, which support up to six SATA ports. The hard drives attached to the SATA connectors follow the spin-up delay described in [Spin-up Delay].

### Debug Header
The motherboard includes a debug header on the front of the motherboard to display [Post Codes]. The debug header supports hot plugging. 

The debug card has two 7-segment LED displays, one RS-232 serial connector, and one reset switch. The RS-232 serial port provides console redirection. The two 7-segment LED displays show BIOS POST code and DIMM error information. The reset switch triggers a system reset when pressed.

The connector for the debug header is a 14-pin, shrouded, right angle, 2mm pitch connector. Figure 11 is an illustration of the headers. The debug card has a key to match with the notch to avoid pin shift when plugging in.

![][fig11]

[fig11]: ../images/amd_debugHeader.png "Figure 11 Debug Header"

_Figure 11 Debug Header_

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
[Figure 12 Debug Header Pin Definition]

#### Post Codes
POST codes are sent to the debug header in hexadecimal format via two hex codes. The hex codes can be driven by either the legacy parallel port (port 80) on the SIO, or 8 GPIO pins. 

During the boot sequence the BIOS initializes and tests each DIMM. If a module fails initialization or does not pass the BIOS test, the following POST codes should flash on the debug card to indicate which DIMM has failed. The first hex character indicates which CPU interfaces the DIMM module; the second hex character indicates the number of the DIMM module. The BIOS flashes the corresponding hex code indefinitely to allow time for a technician to service the system. The DIMM number count starts from the DIMM furthest from the CPU.

&nbsp; | Code | Result                        |
------ | ---- | ----------------------------- | 
CPU0   | A0   | CPU0 DIMM0 (furthest) failure |
       | A1   | CPU0 DIMM1 failure            |
       | A2   | CPU0 DIMM2 failure            |
       | A3   | CPU0 DIMM3 failure            |
       | A4   | CPU0 DIMM4 failure            |
       | A5   | CPU0 DIMM5 failure            |
       | A6   | CPU0 DIMM6 failure            |
       | A7   | CPU0 DIMM7 failure            |
CPU1   | B0   | CPU1 DIMM0 (furthest) failure
       | B1   | CPU1 DIMM1 failure            |
       | B2   | CPU1 DIMM2 failure            |
       | B3   | CPU1 DIMM3 failure            |
       | B4   | CPU1 DIMM4 failure            |
       | B5   | CPU1 DIMM5 failure            |
       | B6   | CPU1 DIMM6 failure            |
       | B7   | CPU1 DIMM7 failure            |
[Figure 13 DIMM Error Code Table]

![][fig14]

[fig14]: ../images/amd_dimm_silkscreen.png "Figure 14 DIMM Numbering Silkscreen"

_Figure 14 DIMM Numbering Silkscreen_

#### Serial Console

The output stage of the system's serial console is contained on the debug card. The TX and RX signals from the SIO are sent to the debug header at the chip's logic levels (+3.3V). The debug card contains the RS-232 level shifter and the RS-232 D-9 connector.

By default, the host does console redirection through serial over LAN (SOL, see 7.3). When the debug card is connected, debug card pin 12 is used to select console redirection between SOL and the local serial port on the card, as described in Figure 12.

### Switches and LEDs

The motherboard includes a power switch, reset switch, power LED, HDD activity LED, and beep error LED.

#### Switches

The front edge of the PCB has right angle pushbutton switches. One switch is used as the system's power button the second switch is used at the system's reset button. 

If the power switch is depressed for less than four seconds, a power management event is issued, indicating that the power switch has been triggered. If the power switch is depressed for more than four seconds, the motherboard performs a hard power off.

If the reset switch is depressed for any length of time, the motherboard performs a hard reset and begins executing the BIOS initialization code.

Each switch is identified by a label on the motherboard's silkscreen. 

#### LEDs
The motherboard has 3 LEDs on the front edge. Figure 15 identifies each LED's color, function, and silkscreen label. The silkscreen describes the functionality of each LED. 

LED Color | Function | Silkscreen Label |
--------- | -------- | ---------------- |
Blue      | Power LED. This LED has the same functionality of a traditional PC power LED. It illuminates only if the motherboard is in the powered on state. | PWR |
Green     | Hard drive activity. This LED illuminates when there is activity on the motherboard's SATA hard drive interfaces. | HDD |
Yellow    | This LED replaces the functionality of the PC speaker. The motherboard causes the LED to illuminate for the same duration and sequence as the PC speaker would normally beep. The LED allows for easier diagnosis in a noisy data center environment. | BEEP |
[Figure 15 LED Functionality]

The beep error LED patterns are described in Figure 16.

Error Description                  | LED Patterns                                                                | | | | | | |
---------------------------------- | --------------------------------------------------------------------------------------- | 
Memory refresh timer error         | On (2s)    | Off (0.25s) | On (2s)    | Off (0.25s) | On (2s)    | Off (3s) | …(repeat) |
Base memory read/write test error  | On (2s)    | Off (0.25s) | On (2s)    | Off (0.25s) | On (0.25s) | Off (3s) | …(repeat) |
Keyboard controller BAT test error | On (0.25s) | Off (0.25s) | On (0.25s) | Off (0.25s) | On (2s)    |          |           | 
General exception error            | On (2s)    | Off (0.25s) | On (0.25s) | Off (0.25s) | On (0.25s) | Off (3s) | …(repeat) | 
Display memory error               | On (0.25s) | Off (0.25s) | On (0.25s) | Off (0.25s) | On (0.25s) |          |           | 
[Figure 16 Beep Error LED Patterns]

Mechanical
----------

### Dimensions

Figure 17 shows the basic view of the Open Compute Project server chassis. Refer to the mechanical step file provided for detailed information.

![][fig17]

[fig17]: ../images/ocp_chassis.png "Figure 17 Open Compute Project Server Chassis for AMD Motherboards"

_Figure 17 Open Compute Project Server Chassis for AMD Motherboards_

### Fixed Locations

Refer to the mechanical DXF file for the fixed locations of the mounting hole, PCI-E x16 slot, and power connector.

### PCB Thickness

To ensure proper alignment of the FCI power connector and mounting within the mechanical enclosure, the PCB thickness of both the motherboard and midplane are 85mil (2.16mm).

### Heat Sinks

The motherboard supports heat sinks that are mounted according to the AMD G34 heat sink specification. The mounting device employs a backplate and receptacles for screw-down type heat sinks. The ODM must comply with all keep out zones defined by AMD. 

### Silkscreen

The silkscreen is white in color and includes labels for these components:

* cpu0/cpu1
* eth0
* DIMM slot numbering
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

The full OCP system meets the following environmental requirements: 

* Altitude up to 1000m above sea level
* System inlet temperature between 18°C and 30°C
* Humidity between 30% and 85%

### Vibration and Shock

The motherboard meets shock and vibration requirements according to the following IEC specifications: IEC78-2-(\*) and IEC721-3-(*) Standard & Levels. The testing requirements are listed in Figure 18.

&nbsp;    | Operating | Non-Operating |
|-------- | --------- | ------------- | 
Vibration | 0.5g acceleration, 1.5mm amplitude, 5 to 500 Hz, 10 sweeps at 1 octave/minute for each of the three axes (one sweep is 5 to 500 to 5 Hz) | 1g acceleration, 3mm amplitude, 5 to 500 Hz, 10 sweeps at 1 octave/minute for each of the three axes (one sweep is 5 to 500 to 5 Hz)
Shock     | 6g, half-sine 11mS, 5 shocks for each of the three axes | 12g, half-sine 11mS, 10 shocks for each of the three axes | 
[Figure 18 Vibration and Shock Requirements]

Prescribed Materials
--------------------

### Disallowed Components
The following components are not used in the design of the motherboard:

* Components disallowed by the European Union's Restriction of Hazardous Substances Directive (RoHS 6)
* Trimmers and/or potentiometers
* Dip switches

### Capacitors and Inductors
The following limitations apply to the use of capacitors:

* Only aluminum organic polymer capacitors made by high quality manufacturers are used; they must be rated 105°C
* All capacitors have a predicted life of at least 50,000 hours at 45°C inlet air temperature, under worst conditions
* Tantalum capacitors are forbidden
* SMT ceramic capacitors with case size > 1206 are forbidden (size 1206 are still allowed when installed far from the PCB edge and with a correct orientation that minimizes risks of cracks) 
* Ceramic material for SMT capacitors must be X7R or better material (COG or NP0 type should be used in critical portions of the motherboard)

Only SMT inductors may be used. The use of through hole inductors is disallowed.



