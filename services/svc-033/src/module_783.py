"""Service module 783: business logic, no crypto."""


def calculate_total_783(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_783():
    return 'module 783 handles orders and invoices'
