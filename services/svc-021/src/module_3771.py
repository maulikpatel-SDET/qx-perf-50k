"""Service module 3771: business logic, no crypto."""


def calculate_total_3771(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3771():
    return 'module 3771 handles orders and invoices'
