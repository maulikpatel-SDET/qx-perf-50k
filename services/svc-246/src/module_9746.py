"""Service module 9746: business logic, no crypto."""


def calculate_total_9746(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9746():
    return 'module 9746 handles orders and invoices'
