"""Service module 27353: business logic, no crypto."""


def calculate_total_27353(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27353():
    return 'module 27353 handles orders and invoices'
