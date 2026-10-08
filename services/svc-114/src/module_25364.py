"""Service module 25364: business logic, no crypto."""


def calculate_total_25364(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25364():
    return 'module 25364 handles orders and invoices'
