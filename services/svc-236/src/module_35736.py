"""Service module 35736: business logic, no crypto."""


def calculate_total_35736(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35736():
    return 'module 35736 handles orders and invoices'
