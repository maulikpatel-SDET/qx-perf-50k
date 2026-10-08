"""Service module 15783: business logic, no crypto."""


def calculate_total_15783(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15783():
    return 'module 15783 handles orders and invoices'
