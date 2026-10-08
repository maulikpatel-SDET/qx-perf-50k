"""Service module 47392: business logic, no crypto."""


def calculate_total_47392(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47392():
    return 'module 47392 handles orders and invoices'
