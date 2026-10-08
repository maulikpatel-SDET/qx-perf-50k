"""Service module 21921: business logic, no crypto."""


def calculate_total_21921(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21921():
    return 'module 21921 handles orders and invoices'
