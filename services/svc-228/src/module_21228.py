"""Service module 21228: business logic, no crypto."""


def calculate_total_21228(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21228():
    return 'module 21228 handles orders and invoices'
