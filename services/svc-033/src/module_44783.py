"""Service module 44783: business logic, no crypto."""


def calculate_total_44783(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44783():
    return 'module 44783 handles orders and invoices'
