"""Service module 36912: business logic, no crypto."""


def calculate_total_36912(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36912():
    return 'module 36912 handles orders and invoices'
