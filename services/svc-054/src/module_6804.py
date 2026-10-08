"""Service module 6804: business logic, no crypto."""


def calculate_total_6804(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6804():
    return 'module 6804 handles orders and invoices'
