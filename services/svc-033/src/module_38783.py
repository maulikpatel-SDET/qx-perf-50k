"""Service module 38783: business logic, no crypto."""


def calculate_total_38783(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38783():
    return 'module 38783 handles orders and invoices'
