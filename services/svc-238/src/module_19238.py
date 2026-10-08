"""Service module 19238: business logic, no crypto."""


def calculate_total_19238(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19238():
    return 'module 19238 handles orders and invoices'
