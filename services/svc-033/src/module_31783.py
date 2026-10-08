"""Service module 31783: business logic, no crypto."""


def calculate_total_31783(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31783():
    return 'module 31783 handles orders and invoices'
