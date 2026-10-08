"""Service module 9771: business logic, no crypto."""


def calculate_total_9771(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9771():
    return 'module 9771 handles orders and invoices'
