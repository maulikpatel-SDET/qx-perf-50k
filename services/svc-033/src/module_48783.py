"""Service module 48783: business logic, no crypto."""


def calculate_total_48783(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48783():
    return 'module 48783 handles orders and invoices'
