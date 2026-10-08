"""Service module 18980: business logic, no crypto."""


def calculate_total_18980(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18980():
    return 'module 18980 handles orders and invoices'
