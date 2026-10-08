"""Service module 10746: business logic, no crypto."""


def calculate_total_10746(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10746():
    return 'module 10746 handles orders and invoices'
