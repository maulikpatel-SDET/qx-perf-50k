"""Service module 24857: business logic, no crypto."""


def calculate_total_24857(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24857():
    return 'module 24857 handles orders and invoices'
