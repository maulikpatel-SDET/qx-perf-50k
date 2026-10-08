"""Service module 27772: business logic, no crypto."""


def calculate_total_27772(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27772():
    return 'module 27772 handles orders and invoices'
