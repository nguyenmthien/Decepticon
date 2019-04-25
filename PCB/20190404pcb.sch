<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="9.1.1">
<drawing>
<settings>
<setting alwaysvectorfont="yes"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
<layer number="2" name="Route2" color="16" fill="1" visible="no" active="no"/>
<layer number="3" name="Route3" color="17" fill="1" visible="no" active="no"/>
<layer number="4" name="Route4" color="18" fill="1" visible="no" active="no"/>
<layer number="5" name="Route5" color="19" fill="1" visible="no" active="no"/>
<layer number="6" name="Route6" color="25" fill="1" visible="no" active="no"/>
<layer number="7" name="Route7" color="26" fill="1" visible="no" active="no"/>
<layer number="8" name="Route8" color="27" fill="1" visible="no" active="no"/>
<layer number="9" name="Route9" color="28" fill="1" visible="no" active="no"/>
<layer number="10" name="Route10" color="29" fill="1" visible="no" active="no"/>
<layer number="11" name="Route11" color="30" fill="1" visible="no" active="no"/>
<layer number="12" name="Route12" color="20" fill="1" visible="no" active="no"/>
<layer number="13" name="Route13" color="21" fill="1" visible="no" active="no"/>
<layer number="14" name="Route14" color="22" fill="1" visible="no" active="no"/>
<layer number="15" name="Route15" color="23" fill="1" visible="no" active="no"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
<layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
<layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
<layer number="20" name="Dimension" color="24" fill="1" visible="no" active="no"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
<layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
<layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
<layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
<layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
<layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
<layer number="51" name="tDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="88" name="SimResults" color="9" fill="1" visible="yes" active="yes"/>
<layer number="89" name="SimProbes" color="9" fill="1" visible="yes" active="yes"/>
<layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="ROBOT_LIBRARY">
<packages>
<package name="ESP32">
<pad name="P$1" x="2.54" y="0" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$2" x="2.54" y="2.54" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$3" x="2.54" y="5.08" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$4" x="2.54" y="7.62" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$5" x="2.54" y="10.16" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$6" x="2.54" y="12.7" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$7" x="2.54" y="15.24" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$8" x="2.54" y="17.78" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$9" x="2.54" y="20.32" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$10" x="2.54" y="22.86" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$11" x="2.54" y="25.4" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$12" x="2.54" y="27.94" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$13" x="2.54" y="30.48" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$14" x="2.54" y="33.02" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$15" x="2.54" y="35.56" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$16" x="-22.86" y="35.56" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$17" x="-22.86" y="33.02" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$18" x="-22.86" y="30.48" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$19" x="-22.86" y="27.94" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$20" x="-22.86" y="25.4" drill="0.7" diameter="1.6764" shape="square" rot="R90"/>
<pad name="P$21" x="-22.86" y="22.86" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$22" x="-22.86" y="20.32" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$23" x="-22.86" y="17.78" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$24" x="-22.86" y="15.24" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$25" x="-22.86" y="12.7" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$26" x="-22.86" y="10.16" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$27" x="-22.86" y="7.62" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$28" x="-22.86" y="5.08" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$29" x="-22.86" y="2.54" drill="0.7" diameter="1.6764" shape="square"/>
<pad name="P$30" x="-22.86" y="0" drill="0.7" diameter="1.6764" shape="square"/>
<wire x1="2.54" y1="-3.81" x2="-25.4" y2="-3.81" width="0.127" layer="21"/>
<wire x1="-25.4" y1="-3.81" x2="-25.4" y2="39.37" width="0.127" layer="21"/>
<wire x1="-25.4" y1="39.37" x2="2.54" y2="39.37" width="0.127" layer="21"/>
<wire x1="2.54" y1="-3.81" x2="5.08" y2="-3.81" width="0.1524" layer="21"/>
<wire x1="5.08" y1="-3.81" x2="5.08" y2="39.37" width="0.1524" layer="21"/>
<wire x1="5.08" y1="39.37" x2="2.54" y2="39.37" width="0.1524" layer="21"/>
<wire x1="5.08" y1="39.37" x2="5.08" y2="41.91" width="0.1524" layer="21"/>
<wire x1="5.08" y1="41.91" x2="-25.4" y2="41.91" width="0.1524" layer="21"/>
<wire x1="-25.4" y1="41.91" x2="-25.4" y2="39.37" width="0.1524" layer="21"/>
<wire x1="-25.4" y1="39.37" x2="-25.4" y2="-10.16" width="0.1524" layer="21"/>
<wire x1="-25.4" y1="-10.16" x2="5.08" y2="-10.16" width="0.1524" layer="21"/>
<wire x1="5.08" y1="-10.16" x2="5.08" y2="-3.81" width="0.1524" layer="21"/>
</package>
<package name="MOTORDRIVER">
<pad name="P$1" x="0" y="0" drill="1.3" diameter="1.6764" shape="square"/>
<pad name="P$2" x="0" y="3.81" drill="1.3" diameter="1.6764" shape="square"/>
<pad name="P$3" x="0" y="7.62" drill="1.3" diameter="1.778" shape="square"/>
<wire x1="-1.27" y1="-2.54" x2="1.27" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="1.27" y1="-2.54" x2="1.27" y2="13.97" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="13.97" x2="-1.27" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="-3.81" x2="7.62" y2="-3.81" width="0.1524" layer="21"/>
<wire x1="7.62" y1="-3.81" x2="7.62" y2="15.24" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="15.24" x2="-2.54" y2="-3.81" width="0.1524" layer="21"/>
<text x="3.81" y="0" size="1.778" layer="21" rot="R90">&gt;NAME</text>
<wire x1="-1.27" y1="13.97" x2="1.27" y2="13.97" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="15.24" x2="7.62" y2="15.24" width="0.1524" layer="21"/>
</package>
<package name="ENCODER">
<pad name="P$1" x="0" y="0" drill="1.3" diameter="1.6764" shape="square"/>
<pad name="P$2" x="0" y="3.81" drill="1.3" diameter="1.6764" shape="square"/>
<pad name="P$3" x="0" y="11.43" drill="1.3" diameter="1.778" shape="square"/>
<wire x1="-1.27" y1="13.97" x2="1.27" y2="13.97" width="0.1524" layer="21"/>
<wire x1="1.27" y1="13.97" x2="1.27" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="1.27" y1="-1.27" x2="-1.27" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="-1.27" x2="-1.27" y2="13.97" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="-2.54" x2="7.62" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="7.62" y1="-2.54" x2="7.62" y2="15.24" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="15.24" x2="7.62" y2="15.24" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="-2.54" x2="-2.54" y2="15.24" width="0.1524" layer="21"/>
<text x="5.08" y="1.27" size="1.778" layer="21" rot="R90">&gt;NAME</text>
</package>
<package name="SOURCE">
<pad name="P$1" x="0" y="0" drill="1.3" diameter="1.778" shape="square"/>
<pad name="P$2" x="0" y="3.81" drill="1.3" diameter="1.778" shape="square"/>
<wire x1="-1.27" y1="-1.27" x2="1.27" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="1.27" y1="-1.27" x2="1.27" y2="5.08" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="5.08" x2="-1.27" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="2.54" y1="-2.54" x2="2.54" y2="6.35" width="0.1524" layer="21"/>
<wire x1="-7.62" y1="6.35" x2="-7.62" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-7.62" y1="-2.54" x2="2.54" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-7.62" y1="6.35" x2="2.54" y2="6.35" width="0.1524" layer="21"/>
<wire x1="1.27" y1="5.08" x2="-1.27" y2="5.08" width="0.1524" layer="21"/>
</package>
</packages>
<symbols>
<symbol name="ESP32">
<pin name="3V3" x="-12.7" y="-17.78" length="middle" rot="R180"/>
<pin name="GND" x="-12.7" y="-15.24" length="middle" rot="R180"/>
<pin name="D15" x="-12.7" y="-12.7" length="middle" rot="R180"/>
<pin name="D2" x="-12.7" y="-10.16" length="middle" rot="R180"/>
<pin name="D4" x="-12.7" y="-7.62" length="middle" rot="R180"/>
<pin name="RX2" x="-12.7" y="-5.08" length="middle" rot="R180"/>
<pin name="TX2" x="-12.7" y="-2.54" length="middle" rot="R180"/>
<pin name="D5" x="-12.7" y="0" length="middle" rot="R180"/>
<pin name="D18" x="-12.7" y="2.54" length="middle" rot="R180"/>
<pin name="D19" x="-12.7" y="5.08" length="middle" rot="R180"/>
<pin name="D21" x="-12.7" y="7.62" length="middle" rot="R180"/>
<pin name="RX0" x="-12.7" y="10.16" length="middle" rot="R180"/>
<pin name="TX0" x="-12.7" y="12.7" length="middle" rot="R180"/>
<pin name="D22" x="-12.7" y="15.24" length="middle" rot="R180"/>
<pin name="D23" x="-12.7" y="17.78" length="middle" rot="R180"/>
<pin name="VIN" x="-38.1" y="-17.78" length="middle"/>
<pin name="GND2" x="-38.1" y="-15.24" length="middle"/>
<pin name="D13" x="-38.1" y="-12.7" length="middle"/>
<pin name="D12" x="-38.1" y="-10.16" length="middle"/>
<pin name="D14" x="-38.1" y="-7.62" length="middle"/>
<pin name="D27" x="-38.1" y="-5.08" length="middle"/>
<pin name="D26" x="-38.1" y="-2.54" length="middle"/>
<pin name="D25" x="-38.1" y="0" length="middle"/>
<pin name="D33" x="-38.1" y="2.54" length="middle"/>
<pin name="D32" x="-38.1" y="5.08" length="middle"/>
<pin name="D35" x="-38.1" y="7.62" length="middle"/>
<pin name="D34" x="-38.1" y="10.16" length="middle"/>
<pin name="VN" x="-38.1" y="12.7" length="middle"/>
<pin name="VP" x="-38.1" y="15.24" length="middle"/>
<pin name="EN" x="-38.1" y="17.78" length="middle"/>
<wire x1="-33.02" y1="20.32" x2="-33.02" y2="-20.32" width="0.254" layer="94"/>
<wire x1="-33.02" y1="-20.32" x2="-17.78" y2="-20.32" width="0.254" layer="94"/>
<wire x1="-17.78" y1="-20.32" x2="-17.78" y2="20.32" width="0.254" layer="94"/>
<wire x1="-17.78" y1="20.32" x2="-33.02" y2="20.32" width="0.254" layer="94"/>
</symbol>
<symbol name="TERMINAL_4_MOTORDRIVER">
<pin name="PWM" x="2.54" y="7.62" length="middle" rot="R180"/>
<pin name="IN2" x="2.54" y="5.08" length="middle" rot="R180"/>
<pin name="IN1" x="2.54" y="2.54" length="middle" rot="R180"/>
<wire x1="-5.08" y1="0" x2="0" y2="0" width="0.1524" layer="94"/>
<wire x1="0" y1="0" x2="0" y2="12.7" width="0.1524" layer="94"/>
<wire x1="0" y1="12.7" x2="-5.08" y2="12.7" width="0.1524" layer="94"/>
<wire x1="-5.08" y1="12.7" x2="-5.08" y2="0" width="0.1524" layer="94"/>
</symbol>
<symbol name="ENCODER">
<pin name="GND" x="2.54" y="2.54" length="middle" rot="R180"/>
<pin name="CHA" x="2.54" y="5.08" length="middle" rot="R180"/>
<pin name="V+" x="2.54" y="10.16" length="middle" rot="R180"/>
<wire x1="-5.08" y1="0" x2="0" y2="0" width="0.1524" layer="94"/>
<wire x1="0" y1="0" x2="0" y2="12.7" width="0.1524" layer="94"/>
<wire x1="0" y1="12.7" x2="-5.08" y2="12.7" width="0.1524" layer="94"/>
<wire x1="-5.08" y1="12.7" x2="-5.08" y2="0" width="0.1524" layer="94"/>
</symbol>
<symbol name="SOURCE">
<pin name="GND" x="2.54" y="5.08" length="middle" rot="R180"/>
<pin name="V+" x="2.54" y="2.54" length="middle" rot="R180"/>
<wire x1="-5.08" y1="0" x2="0" y2="0" width="0.1524" layer="94"/>
<wire x1="0" y1="0" x2="0" y2="7.62" width="0.1524" layer="94"/>
<wire x1="0" y1="7.62" x2="-5.08" y2="7.62" width="0.1524" layer="94"/>
<wire x1="-5.08" y1="0" x2="-5.08" y2="7.62" width="0.1524" layer="94"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="ESP32">
<gates>
<gate name="G$1" symbol="ESP32" x="17.78" y="20.32"/>
</gates>
<devices>
<device name="" package="ESP32">
<connects>
<connect gate="G$1" pin="3V3" pad="P$1"/>
<connect gate="G$1" pin="D12" pad="P$27"/>
<connect gate="G$1" pin="D13" pad="P$28"/>
<connect gate="G$1" pin="D14" pad="P$26"/>
<connect gate="G$1" pin="D15" pad="P$3"/>
<connect gate="G$1" pin="D18" pad="P$9"/>
<connect gate="G$1" pin="D19" pad="P$10"/>
<connect gate="G$1" pin="D2" pad="P$4"/>
<connect gate="G$1" pin="D21" pad="P$11"/>
<connect gate="G$1" pin="D22" pad="P$14"/>
<connect gate="G$1" pin="D23" pad="P$15"/>
<connect gate="G$1" pin="D25" pad="P$23"/>
<connect gate="G$1" pin="D26" pad="P$24"/>
<connect gate="G$1" pin="D27" pad="P$25"/>
<connect gate="G$1" pin="D32" pad="P$21"/>
<connect gate="G$1" pin="D33" pad="P$22"/>
<connect gate="G$1" pin="D34" pad="P$19"/>
<connect gate="G$1" pin="D35" pad="P$20"/>
<connect gate="G$1" pin="D4" pad="P$5"/>
<connect gate="G$1" pin="D5" pad="P$8"/>
<connect gate="G$1" pin="EN" pad="P$16"/>
<connect gate="G$1" pin="GND" pad="P$2"/>
<connect gate="G$1" pin="GND2" pad="P$29"/>
<connect gate="G$1" pin="RX0" pad="P$12"/>
<connect gate="G$1" pin="RX2" pad="P$6"/>
<connect gate="G$1" pin="TX0" pad="P$13"/>
<connect gate="G$1" pin="TX2" pad="P$7"/>
<connect gate="G$1" pin="VIN" pad="P$30"/>
<connect gate="G$1" pin="VN" pad="P$18"/>
<connect gate="G$1" pin="VP" pad="P$17"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="MOTORDRIVER">
<gates>
<gate name="G$1" symbol="TERMINAL_4_MOTORDRIVER" x="0" y="0"/>
</gates>
<devices>
<device name="" package="MOTORDRIVER">
<connects>
<connect gate="G$1" pin="IN1" pad="P$3"/>
<connect gate="G$1" pin="IN2" pad="P$2"/>
<connect gate="G$1" pin="PWM" pad="P$1"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="ENCODER">
<gates>
<gate name="G$1" symbol="ENCODER" x="0" y="0"/>
</gates>
<devices>
<device name="" package="ENCODER">
<connects>
<connect gate="G$1" pin="CHA" pad="P$2"/>
<connect gate="G$1" pin="GND" pad="P$3"/>
<connect gate="G$1" pin="V+" pad="P$1"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="SOURCE">
<gates>
<gate name="G$1" symbol="SOURCE" x="0" y="0"/>
</gates>
<devices>
<device name="" package="SOURCE">
<connects>
<connect gate="G$1" pin="GND" pad="P$2"/>
<connect gate="G$1" pin="V+" pad="P$1"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="U$1" library="ROBOT_LIBRARY" deviceset="ESP32" device=""/>
<part name="RM" library="ROBOT_LIBRARY" deviceset="MOTORDRIVER" device=""/>
<part name="LM" library="ROBOT_LIBRARY" deviceset="MOTORDRIVER" device=""/>
<part name="RE" library="ROBOT_LIBRARY" deviceset="ENCODER" device=""/>
<part name="LE" library="ROBOT_LIBRARY" deviceset="ENCODER" device=""/>
<part name="U$9" library="ROBOT_LIBRARY" deviceset="SOURCE" device=""/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="U$1" gate="G$1" x="110.49" y="97.79"/>
<instance part="RM" gate="G$1" x="118.11" y="116.84" rot="R180"/>
<instance part="LM" gate="G$1" x="118.11" y="97.79" rot="R180"/>
<instance part="RE" gate="G$1" x="48.26" y="104.14"/>
<instance part="LE" gate="G$1" x="49.53" y="85.09"/>
<instance part="U$9" gate="G$1" x="55.88" y="62.23" rot="R90"/>
</instances>
<busses>
</busses>
<nets>
<net name="N$2" class="0">
<segment>
<pinref part="RE" gate="G$1" pin="CHA"/>
<pinref part="U$1" gate="G$1" pin="D14"/>
<wire x1="72.39" y1="90.17" x2="64.77" y2="90.17" width="0.1524" layer="91"/>
<wire x1="64.77" y1="90.17" x2="64.77" y2="110.49" width="0.1524" layer="91"/>
<wire x1="64.77" y1="110.49" x2="52.07" y2="110.49" width="0.1524" layer="91"/>
<wire x1="52.07" y1="110.49" x2="50.8" y2="109.22" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$4" class="0">
<segment>
<pinref part="LE" gate="G$1" pin="GND"/>
<wire x1="52.07" y1="87.63" x2="39.37" y2="87.63" width="0.1524" layer="91"/>
<wire x1="39.37" y1="87.63" x2="39.37" y2="82.55" width="0.1524" layer="91"/>
<pinref part="RE" gate="G$1" pin="GND"/>
<wire x1="39.37" y1="87.63" x2="39.37" y2="106.68" width="0.1524" layer="91"/>
<wire x1="39.37" y1="106.68" x2="50.8" y2="106.68" width="0.1524" layer="91"/>
<junction x="39.37" y="87.63"/>
<pinref part="U$1" gate="G$1" pin="GND2"/>
<wire x1="72.39" y1="82.55" x2="39.37" y2="82.55" width="0.1524" layer="91"/>
<pinref part="U$9" gate="G$1" pin="GND"/>
<wire x1="52.07" y1="87.63" x2="50.8" y2="87.63" width="0.1524" layer="91"/>
<wire x1="50.8" y1="87.63" x2="50.8" y2="64.77" width="0.1524" layer="91"/>
<junction x="52.07" y="87.63"/>
</segment>
</net>
<net name="N$5" class="0">
<segment>
<pinref part="LE" gate="G$1" pin="CHA"/>
<pinref part="U$1" gate="G$1" pin="D13"/>
<wire x1="72.39" y1="85.09" x2="59.69" y2="85.09" width="0.1524" layer="91"/>
<wire x1="59.69" y1="85.09" x2="59.69" y2="90.17" width="0.1524" layer="91"/>
<wire x1="59.69" y1="90.17" x2="52.07" y2="90.17" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$6" class="0">
<segment>
<pinref part="LE" gate="G$1" pin="V+"/>
<wire x1="36.83" y1="78.74" x2="36.83" y2="95.25" width="0.1524" layer="91"/>
<wire x1="36.83" y1="95.25" x2="52.07" y2="95.25" width="0.1524" layer="91"/>
<pinref part="RE" gate="G$1" pin="V+"/>
<wire x1="36.83" y1="95.25" x2="36.83" y2="114.3" width="0.1524" layer="91"/>
<wire x1="36.83" y1="114.3" x2="50.8" y2="114.3" width="0.1524" layer="91"/>
<junction x="36.83" y="95.25"/>
<pinref part="U$1" gate="G$1" pin="VIN"/>
<wire x1="72.39" y1="80.01" x2="72.39" y2="78.74" width="0.1524" layer="91"/>
<wire x1="72.39" y1="78.74" x2="53.34" y2="78.74" width="0.1524" layer="91"/>
<wire x1="53.34" y1="78.74" x2="36.83" y2="78.74" width="0.1524" layer="91"/>
<pinref part="U$9" gate="G$1" pin="V+"/>
<wire x1="53.34" y1="78.74" x2="53.34" y2="63.5" width="0.1524" layer="91"/>
<wire x1="53.34" y1="63.5" x2="53.34" y2="64.77" width="0.1524" layer="91"/>
<junction x="53.34" y="78.74"/>
</segment>
</net>
<net name="N$9" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="D15"/>
<wire x1="97.79" y1="85.09" x2="104.14" y2="85.09" width="0.1524" layer="91"/>
<wire x1="104.14" y1="85.09" x2="104.14" y2="96.52" width="0.1524" layer="91"/>
<pinref part="LM" gate="G$1" pin="IN1"/>
<wire x1="104.14" y1="96.52" x2="115.57" y2="96.52" width="0.1524" layer="91"/>
<wire x1="115.57" y1="96.52" x2="115.57" y2="95.25" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$10" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="D2"/>
<wire x1="97.79" y1="87.63" x2="106.68" y2="87.63" width="0.1524" layer="91"/>
<wire x1="106.68" y1="87.63" x2="106.68" y2="93.98" width="0.1524" layer="91"/>
<pinref part="LM" gate="G$1" pin="IN2"/>
<wire x1="106.68" y1="93.98" x2="115.57" y2="93.98" width="0.1524" layer="91"/>
<wire x1="115.57" y1="93.98" x2="115.57" y2="92.71" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$11" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="D4"/>
<wire x1="97.79" y1="90.17" x2="115.57" y2="90.17" width="0.1524" layer="91"/>
<wire x1="115.57" y1="90.17" x2="115.57" y2="91.44" width="0.1524" layer="91"/>
<pinref part="LM" gate="G$1" pin="PWM"/>
<junction x="115.57" y="90.17"/>
</segment>
</net>
<net name="N$12" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="RX2"/>
<wire x1="97.79" y1="92.71" x2="102.87" y2="92.71" width="0.1524" layer="91"/>
<wire x1="102.87" y1="92.71" x2="102.87" y2="114.3" width="0.1524" layer="91"/>
<pinref part="RM" gate="G$1" pin="IN1"/>
<wire x1="102.87" y1="114.3" x2="115.57" y2="114.3" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$13" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="TX2"/>
<wire x1="97.79" y1="95.25" x2="101.6" y2="95.25" width="0.1524" layer="91"/>
<pinref part="RM" gate="G$1" pin="IN2"/>
<wire x1="101.6" y1="95.25" x2="101.6" y2="111.76" width="0.1524" layer="91"/>
<wire x1="101.6" y1="111.76" x2="115.57" y2="111.76" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$14" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="D5"/>
<wire x1="97.79" y1="97.79" x2="105.41" y2="97.79" width="0.1524" layer="91"/>
<wire x1="105.41" y1="97.79" x2="105.41" y2="109.22" width="0.1524" layer="91"/>
<pinref part="RM" gate="G$1" pin="PWM"/>
<wire x1="105.41" y1="109.22" x2="115.57" y2="109.22" width="0.1524" layer="91"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
</eagle>
