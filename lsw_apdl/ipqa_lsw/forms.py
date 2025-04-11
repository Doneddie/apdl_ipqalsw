from django import forms
from django.core.exceptions import ValidationError
from django_summernote.widgets import SummernoteWidget
from datetime import datetime

SHIFT_CHOICES = [
    ('1st', '1st SHIFT'),
    ('2nd', '2nd SHIFT'),
    ('3rd', '3rd SHIFT'),
    ('GEN', 'GEN SHIFT'),
]

SECTION_CHOICES = [
    ('STORES', 'STORES'),
    ('WTP', 'WATER TREATMENT PLANT'),
    ('DISPENSING', 'DISPENSING'),
    ('CLEAN_ROOM', 'CLEAN ROOM'),
    ('STERILIZATION', 'STERILIZATION'),
    ('PACKING', 'PACKING'),
]

class LeaderStandardWorkForm(forms.Form):
    # -- General Information --
    name = forms.CharField(label="NAME *", max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    shift = forms.ChoiceField(label="SHIFT *", choices=SHIFT_CHOICES, required=True,  widget=forms.CheckboxSelectMultiple)
    date = forms.DateField(
        label="DATE *", required=True,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    sections_supervised = forms.MultipleChoiceField(
        label="SECTION(S) SUPERVISED *",
        choices=SECTION_CHOICES, required=True,
        widget=forms.CheckboxSelectMultiple
    )

    # -- STORES Section --
    tick_all_stores = forms.BooleanField(label="Tick All Stores Checks", required=False)
    stores_cleanliness = forms.BooleanField(label="Cleanliness of Area", required=False)
    stores_environmental = forms.BooleanField(label="Environmental Monitoring", required=False)
    stores_line_clearance = forms.BooleanField(label="Verify Proper Line Clearance", required=False)
    stores_calibration = forms.BooleanField(label="Verify Calibration of Balances", required=False)
    stores_material_received = forms.BooleanField(label="Check Material Received (RM/PM)", required=False)
    stores_supervise_sampling = forms.BooleanField(label="Supervise Sampling", required=False)
    stores_material_issued = forms.BooleanField(label="Check Material Issued", required=False)
    stores_released_rm = forms.BooleanField(label="Released RM Used", required=False)
    stores_status_board = forms.BooleanField(label="Status Board Update", required=False)
    stores_bmr_online = forms.BooleanField(label="BMR Online Filling", required=False)
    stores_logbooks = forms.BooleanField(label="Verification of Logbooks", required=False)
    stores_verify_rejections = forms.BooleanField(label="Check / Verify Rejections", required=False)
    stores_status_labels = forms.BooleanField(label="Check for Status Labels", required=False)
    stores_batches_received = forms.BooleanField(label="Verify Batches Received from Packing", required=False)
    stores_aql_checks = forms.BooleanField(label="AQL Checks on Batches Sold", required=False)
    stores_report = forms.CharField(
        label="STORES Report/Escalation: Write any reports or escalations and include actions taken in brackets",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=False
    )

    # -- Water Treatment Plant Section --
    tick_all_wtp = forms.BooleanField(label="Tick All WTP Checks", required=False)
    wtp_cleanliness = forms.BooleanField(label="Cleanliness of Area", required=False)
    wtp_verify_ro_water_generation_report = forms.BooleanField(label="Verify RO Water Generation Report", required=False)
    wtp_verify_wfi_system_report = forms.BooleanField(label="Verify WFI System Report", required=False)
    wtp_verify_rowd_report = forms.BooleanField(label="Verify ROWD Report", required=False)
    wtp_verification_of_logbooks = forms.BooleanField(label="Verification of Logbooks", required=False)
    wtp_report = forms.CharField(
        label="Water Treatment Plant Report/Escalation: Write any reports or escalations and include actions taken in brackets",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=False
    )

    # -- Dispensing Section --
    tick_all_dispensing = forms.BooleanField(label="Tick All Dispensing Checks", required=False)
    dispensing_cleanliness = forms.BooleanField(label="Cleanliness of Area", required=False)
    dispensing_environmental = forms.BooleanField(label="Environmental Monitoring", required=False)
    dispensing_calibration = forms.BooleanField(label="Verify Calibration of Balances", required=False)
    dispensing_supervise = forms.BooleanField(label="Supervise Dispensing", required=False)
    dispensing_released_rm = forms.BooleanField(label="Released RM Used", required=False)
    dispensing_status_board = forms.BooleanField(label="Status Board Update", required=False)
    dispensing_bmr_online = forms.BooleanField(label="BMR Online Filling", required=False)
    dispensing_logbooks = forms.BooleanField(label="Verification of Logbooks", required=False)
    dispensing_report = forms.CharField(
        label="DISPENSING Report/Escalation: Write any reports or escalations and include actions taken in brackets",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=False
    )

    # -- Clean Room Section --
    tick_all_cleanroom = forms.BooleanField(label="Tick All Clean Room Checks", required=False)
    cleanroom_cleanliness = forms.BooleanField(label="Cleanliness of Area", required=False)
    cleanroom_status_board = forms.BooleanField(label="Status Board Update", required=False)
    cleanroom_gowning = forms.BooleanField(label="Check Proper Gowning", required=False)
    cleanroom_bmr_online = forms.BooleanField(label="BMR Online Filling", required=False)
    cleanroom_logbooks = forms.BooleanField(label="Verification of Logbooks", required=False)
    cleanroom_footwear = forms.BooleanField(label="Check Cleaning of Footwear", required=False)
    cleanroom_filter = forms.BooleanField(label="Verify Filter Integrity", required=False)
    cleanroom_cip = forms.BooleanField(label="Sample/Verify CIP/SIP", required=False)
    cleanroom_bulk = forms.BooleanField(label="Sample and Follow-up Bulk", required=False)
    cleanroom_bottle_batch = forms.BooleanField(label="Check Bottle Batch Coding", required=False)
    cleanroom_bioburden = forms.BooleanField(label="Sample BioBurden for E/E/N", required=False)
    cleanroom_line_clearance = forms.BooleanField(label="Verify Proper Line Clearance", required=False)
    cleanroom_report = forms.CharField(
        label="CLEAN ROOM Report/Escalation: Write any reports or escalations and include actions taken in brackets",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=False
    )

    # -- Sterilization Section --
    tick_all_sterilization = forms.BooleanField(label="Tick All Sterilization Checks", required=False)
    sterilization_cleanliness = forms.BooleanField(label="Cleanliness of Area", required=False)
    sterilization_line_clearance = forms.BooleanField(label="Verify Proper Line Clearance", required=False)
    sterilization_status_board = forms.BooleanField(label="Status Board Update", required=False)
    sterilization_calibration = forms.BooleanField(label="Verify Calibration of Balances", required=False)
    sterilization_bmr_online = forms.BooleanField(label="BMR Online Filling", required=False)
    sterilization_logbooks = forms.BooleanField(label="Verification of Logbooks", required=False)
    sterilization_verify_rejections = forms.BooleanField(label="Check / Verify Rejections", required=False)
    sterilization_bottle_batch = forms.BooleanField(label="Check Bottle Batch Coding", required=False)
    sterilization_volume = forms.BooleanField(label="Check Volumes on Time", required=False)
    sterilization_bioburden = forms.BooleanField(label="Sample BioBurden", required=False)
    sterilization_leak_testing = forms.BooleanField(label="Verify Leak Testing Status", required=False)
    sterilization_finished = forms.BooleanField(label="Sample Finished Products", required=False)
    sterilization_report = forms.CharField(
        label="STERILIZATION Report/Escalation: Write any reports or escalations and include actions taken in brackets",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=False
    )

    # -- Packing Section --
    tick_all_packing= forms.BooleanField(label="Tick All Packing Checks", required=False)
    packing_cleanliness = forms.BooleanField(label="Cleanliness of Area", required=False)
    packing_calibration = forms.BooleanField(label="Verify Calibration of Balances", required=False)
    packing_material_received = forms.BooleanField(label="Check Material Received (PM)", required=False)
    packing_line_clearance = forms.BooleanField(label="Verify Proper Line Clearance", required=False)
    packing_status_board = forms.BooleanField(label="Status Board Update", required=False)
    packing_bmr_online = forms.BooleanField(label="BMR Online Filling", required=False)
    packing_leak_testing = forms.BooleanField(label="Verify Leak Testing Status", required=False)
    packing_visual = forms.BooleanField(label="Verify Proper Visual Inspection Done", required=False)
    packing_bottle_batch = forms.BooleanField(label="Check Bottle Batch Coding", required=False)
    packing_quality = forms.BooleanField(label="Check Quality of BOPP Wrapping", required=False)
    packing_labels = forms.BooleanField(label="Check Labels Pasted on C. Boxes", required=False)
    packing_weight_limits = forms.BooleanField(label="Provide Weight Limits", required=False)
    packing_retention = forms.BooleanField(label="Pick Retention Samples", required=False)
    packing_logbooks = forms.BooleanField(label="Verification of Logbooks", required=False)
    packing_verify_rejections = forms.BooleanField(label="Check / Verify Rejections", required=False)
    packing_status_labels = forms.BooleanField(label="Check for Status Labels", required=False)
    packing_report = forms.CharField(
        label="PACKING Report/Escalation: Write any reports or escalations and include actions taken in brackets",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=False
    )

    # -- Periodic Duties Section --
    tick_all_periodic = forms.BooleanField(label="Tick All Periodic Checks", required=False)
    periodic_trainings = forms.BooleanField(label="Trainings", required=False)
    periodic_investigations = forms.BooleanField(label="Investigations", required=False)
    periodic_equipment_tags = forms.BooleanField(label="Check Equipment Tags", required=False)
    periodic_validation = forms.BooleanField(label="Check Validation Status", required=False)
    periodic_calibration = forms.BooleanField(label="Check Calibration Status", required=False)
    periodic_colour_coding = forms.BooleanField(label="Check Colour Coding", required=False)
    periodic_lighting = forms.BooleanField(label="Check Lighting in Visual Inspection Booth", required=False)
    periodic_cleanroom_qual = forms.BooleanField(label="Cleanroom Personnel Qualification", required=False)
    periodic_report = forms.CharField(
        label="PERIODIC DUTIES Report/Escalation: Write any reports or escalations and include actions taken in brackets",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=False
    )
