"""Service module 43783: business logic, no crypto."""


def calculate_total_43783(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43783():
    return 'module 43783 handles orders and invoices'
