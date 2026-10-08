"""Service module 44965: business logic, no crypto."""


def calculate_total_44965(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44965():
    return 'module 44965 handles orders and invoices'
