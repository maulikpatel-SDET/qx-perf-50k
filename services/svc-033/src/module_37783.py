"""Service module 37783: business logic, no crypto."""


def calculate_total_37783(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37783():
    return 'module 37783 handles orders and invoices'
