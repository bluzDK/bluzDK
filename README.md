<p align="center" >
<img src="http://bluz.io/static/img/logo.png" alt="GoGlove" title="GoGlove">
</p>

Bluz DK Hardware Files
==========
Bluz is a Development Kit (DK) that implements the Wiring language and talks to the [Particle](https://www.particle.io/) cloud through Bluetooth Low Energy. It can be accessed through a REST API and programmed from a Web IDE.

These files have been made available online through a [Creative Commons Attribution-ShareAlike 3.0](http://creativecommons.org/licenses/by-sa/3.0/) license.

You are welcome to distribute, remix, and use these files for commercial purposes. If you do so, please attribute the original design to Bluz both on the website and on the physical packaging of the product or in the instruction manual. All derivative works must be published under the same or a similar license.

All items are subject to change over time as the product is designed, so make sure you are always looking at the latest information by pulling often.

##Sections
<b>BOM</b>: Current Bill of Materials for bluz.

<b>Datasheets</b>: Datasheets for all major parts on the board, including the nrf51822 and the MDBT40 module that it uses.

<b>HW Design</b>: Schematics, board layouts, and other design files.

<b>HW Libraries</b>: Eagle CAD libraries for the components used on Bluz DK.

<b>Pin Mapping</b>: Pin mapping diagram for Bluz.

##Tech Specs
<p>Hardware</p>
<ul>
    <li>Nordic Semiconductor nRF51822 SoC</li>
    <li>ARM Cortex M0, 16MHz</li>
    <li>32KB RAM, 256KB FLASH</li>
    <li>Bluetooth LE 4.1</li>
    <li>10 bit ADC</li>
    <li>256KB External FLASH</li>
    <li>3.0V-6V (3.3V compatible)</li>
</ul>
<p>Power Consumption</p>
<ul>
    <li>Connected/Standby: 60uA</li>
    <li>Transmitting Max: 18mA</li>
</ul>
<p>Typical Range (subject to environment):</p>
<ul>
    <li>Indoors: 60-100 feet</li>
    <li>Outdoors: 150-200 feet</li>
</ul>
<p>Software</p>
<ul>
    <li>Spark Web IDE</li>
    <li>Wiring (same as Arduino)</li>
    <li>Native C/C++ Programming</li>
    <li>GCC ARM</li>
    <li>Assembly (if you're that bold)</li>
</ul>
<p>Cloud</p>
<ul>
    <li>Spark Connected</li>
    <li>IFTTT Integrated</li>
    <li>IPv6 Support</li>
    <li>Remote programmable through Spark Cloud</li>
    <li>Control via REST API</li>
</ul>